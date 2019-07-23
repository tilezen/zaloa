import boto3
import botocore.exceptions
import datetime
import fnmatch
import json
import posixpath
from flask import abort, request


MEMORY_CACHE_TTL = 900 # 15 minutes


def register_auth(app):
    if app.config.get("APIKEY_METHOD") == "s3":
        api_key_bucket = app.config.get('APIKEY_S3_BUCKET')
        if not api_key_bucket:
            raise ValueError("Need to set APIKEY_S3_BUCKET when APIKEY_METHOD is set to 's3'")

        api_key_key_prefix = app.config.get('APIKEY_S3_KEY_PREFIX')
        auth_provider = S3ApiKeyAuthMethod(
            app.logger.getChild('auth'),
            api_key_bucket,
            api_key_key_prefix,
        )
        app.before_request(auth_provider.handle_request)
        app.logger.info("Using S3 API key auth method")
    else:
        app.logger.info("No auth method loaded")


def is_origin_allowed(allowed_origins, origin):
    if not allowed_origins:
        # If the key doesn't specify any allowed origins then let everything through
        return True

    if not origin:
        # If the key specifies allowed origins but none is specified then don't allow it
        return False

    # Check the list of allowed origins against the given origin
    for allowed_origin in allowed_origins:
        if fnmatch.fnmatch(origin, allowed_origin):
            return True

    # If nothing is found, then don't let it through
    return False


class S3ApiKeyAuthMethod(object):
    def __init__(self, logger, bucket, prefix):
        self.logger = logger
        self.bucket = bucket
        self.prefix = prefix
        self.keys = {}
        self.s3 = boto3.resource('s3')
        self.invalid_marker = {'valid': False}

    def get_key_data(self, api_key):
        if '/' in api_key or '.' in api_key:
            self.keys[api_key] = self.invalid_marker
            return self.invalid_marker

        key_data = self.keys.get(api_key)

        now = datetime.datetime.utcnow()
        last_fetched = None
        if key_data:
            last_fetched = key_data.get('last_fetched')
            key_age = (now - last_fetched).total_seconds()

            if key_age < MEMORY_CACHE_TTL:
                # If the cached key data is new enough, no need to check S3 again
                return key_data

        obj = self.s3.Object(self.bucket, posixpath.join(self.prefix, 'keys', api_key))
        try:
            if last_fetched:
                resp = obj.get(IfModifiedSince=last_fetched)
            else:
                resp = obj.get()

            data_str = resp['Body'].read().decode('utf8')
            key_data = json.loads(data_str)

            key_data['valid'] = True
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                # We don't know about this key in S3
                key_data = {'valid': False}
            elif e.response['Error']['Code'] == '304':
                # No change since last fetched
                pass
            else:
                self.logger.info("Client error for key %s: %s", api_key, e)
                return self.invalid_marker

        # Cache the result
        key_data['last_fetched'] = now
        self.keys[api_key] = key_data

        return key_data


    def handle_request(self):
        if request.path in ('/health_check', '/preview.html'):
            # Let healthcheck and preview through without api key
            return

        api_key = request.args.get('api_key')

        if not api_key:
            abort(403, "api_key is missing")

        key_data = self.get_key_data(api_key)
        if not key_data or key_data['valid'] == False:
            abort(403, "invalid api key")

        if key_data.get('enabled') == False:
            abort(403, "disabled api key")

        origin = request.headers.get('origin')
        if not is_origin_allowed(key_data.get('allowed_origins'), origin):
            abort(403, "origin is not allowed by this api key")

        return
