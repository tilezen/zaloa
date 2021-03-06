import os


CORS_SEND_WILDCARD = True

# The max age for tiles returned by this service. Clients (both browsers and intermediate caches like CloudFront) will
# cache the tile this many seconds before checking with the origin to get a new tile.
# http://werkzeug.pocoo.org/docs/0.14/datastructures/#werkzeug.datastructures.ResponseCacheControl.max_age
CACHE_MAX_AGE = int(os.environ.get("CACHE_MAX_AGE", '1200'))

# The "shared" max age for tiles returned by this service. When an object is beyond this age in a shared cache (like CloudFront),
# the shared cache should check with the origin to see if the object was updated. In general, this number should be smaller than
# the max age set above.
# http://werkzeug.pocoo.org/docs/0.14/datastructures/#werkzeug.datastructures.ResponseCacheControl.s_maxage
SHARED_CACHE_MAX_AGE = int(os.environ.get("SHARED_CACHE_MAX_AGE", '600'))

CACHE_TYPE = os.environ.get('CACHE_TYPE', 'null')
CACHE_NO_NULL_WARNING = True
# Expose some of the caching config via environment variables
# so we can have more freedom to configure this in-situ.
CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL')
CACHE_THRESHOLD = int(os.environ.get('CACHE_THRESHOLD')) if os.environ.get('CACHE_THRESHOLD') else None
CACHE_KEY_PREFIX = os.environ.get('CACHE_KEY_PREFIX')
CACHE_DIR = os.environ.get('CACHE_DIR')

# This can be 's3' or 'http'
TILES_FETCH_METHOD = os.environ.get('TILES_FETCH_METHOD')
TILES_S3_BUCKET = os.environ.get("TILES_S3_BUCKET")
TILES_HTTP_PREFIX = os.environ.get("TILES_HTTP_PREFIX")
REQUESTER_PAYS = os.environ.get("REQUESTER_PAYS", 'false') == 'true'
