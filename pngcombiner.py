from __future__ import print_function

from cStringIO import StringIO
from PIL import Image
from time import time
import base64
import boto3
import json
import math
import os


def is_valid(z, x, y):
    if z < 0 or x < 0 or y < 0:
        return False
    if z > 15:
        return False
    x_y_limit = int(math.pow(2, z))
    if x >= x_y_limit or y >= x_y_limit:
        return False
    return True


def log(request_state):
    print(json.dumps(request_state))


class MissingTileException(Exception):
    """
    Required tile missing

    Particular type of exception to represent a tile we expected to be
    there is missing
    """

    def __init__(self, z, x, y):
        super(MissingTileException, self).__init__('Missing tiles: %d/%d/%d' % z, x, y)
        self.z = z
        self.x = x
        self.y = y


def lambda_handler(event, context):
    start_total = time()
    request_state = {}

    request_state['timing'] = {}

    # NOTE: this needs to be set as an environment variable in the handler
    bucket = os.environ['S3_BUCKET']

    status = 200
    # these will get set conditionally based on the path
    # and status will be updated appropriately
    reason_not_found = ''
    reason_error = ''
    response = ''

    # TODO update the path parsing to detect the appropriate request type
    tile_path = request_state['path'] = event['tile']
    path_parts = tile_path.split('/')
    z = x = y = fmt = None
    if len(path_parts) == 3:
        z_s, x_s, y_fmt = path_parts
        y_fmt_parts = y_fmt.split('.')
        if len(y_fmt_parts) == 2:
            y_s, fmt = y_fmt_parts
        try:
            z = request_state['z'] = int(z_s)
            x = request_state['x'] = int(x_s)
            y = request_state['y'] = int(y_s)
        except ValueError:
            pass

    if y is None or fmt != 'png' or not is_valid(z, x, y):
        status = 404
        reason_not_found = 'Invalid url path'

    # TODO assume that the requests are just for 512 tiles currently
    request_state['request_type'] = request_type = 'terrarium-512'

    try:
        if request_type == 'terrarium-512':
            response, timing_metadata = handle_terrarium(bucket, z, x, y)
            request_state['timing'].update(timing_metadata)
        else:
            reason_error = 'Invalid request type: ' + request_type
            status = 500

    except Exception as e:
        if isinstance(e, MissingTileException):
            request_state['missing_tile'] = dict(
                z=e.z,
                x=e.x,
                y=e.y,
            )
        status = 500
        # this logs any unexpected exceptions to the log, and will
        # provide a stack trace
        import traceback
        traceback.print_exc()
        reason_error = str(e)

    # add in total timing information
    stop_total = time()
    time_total = stop_total - start_total
    request_state['timing']['total'] = time_total

    # finalize request state and log it
    request_state['status'] = status
    if status == 404:
        request_state['error'] = reason_not_found
    elif status == 500:
        request_state['error'] = reason_error
    log(request_state)

    # return the appropriate response
    if status == 404:
        raise Exception('Status: 404 - %s' % reason_not_found)
    elif status == 500:
        raise Exception('Status: 500 - %s' % reason_error)
    else:
        return response


def handle_terrarium(bucket, z, x, y):
    # generate the list of tiles that need to get fetched
    z_256 = z + 1
    y_256 = y * 2
    x_256 = x * 2
    tiles_256 = (
        (z_256, y_256, x_256),
        (z_256, y_256, x_256 + 1),
        (z_256, y_256 + 1, x_256),
        (z_256, y_256 + 1, x_256 + 1),
    )
    # the offsets in the resulting 512 image used for PIL
    locations = (
        (0, 0),
        (0, 256),
        (256, 0),
        (256, 256),
    )
    tile_contents = []

    timing_metadata = dict(
        fetch={},
        process={},
    )
    s3_client = boto3.client('s3')
    # TODO support cache headers for 304 responses?
    start_fetch_total = time()
    for z, x, y in tiles_256:
        # TODO terrarium/normal should come from the url
        key = 'terrarium/%d/%d/%d.png' % (z, x, y)
        # TODO
        # raises an exception if it doesn't exist
        # ERROR handling!
        start_fetch_tile = time()
        try:
            resp = s3_client.get_object(
                Bucket=bucket,
                Key=key,
            )
        except Exception as e:
            # we got some kind of exception, this will early out of the function
            try:
                # check to see if the exception is a 404 and call that out specially
                if e.response['Error']['Code'] == 'NoSuchKey':
                    # opt to return these more specifically as an exception
                    # we want to early out in all cases, but we might want to know about missing tiles in particular
                    raise MissingTileException(z, x, y)
            except:
                pass
            # different exception, treat as 500
            raise e

        body_file = resp['Body']
        content = body_file.read()
        body_file.close()
        stop_fetch_tile = time()
        tile_contents.append(content)
        time_fetch_tile = stop_fetch_tile - start_fetch_tile
        timing_metadata['fetch']['%d/%d/%d' % (z, x, y)] = time_fetch_tile

    stop_fetch_total = time()
    time_fetch_total = stop_fetch_total - start_fetch_total
    timing_metadata['fetch']['total'] = time_fetch_total

    start_process_total = time()
    result_image = Image.new('RGB', (512, 512))
    for tile_content, location, (z, x, y) in zip(tile_contents, locations, tiles_256):
        start_process_tile = time()
        tile_fp = StringIO(tile_content)
        img = Image.open(tile_fp)
        result_image.paste(img, location)
        stop_process_tile = time()
        time_process_tile = stop_process_tile - start_process_tile
        timing_metadata['process']['%d/%d/%d' % (z, x, y)] = time_process_tile
    stop_process_total = time()
    time_process_total = stop_process_total - start_process_total
    timing_metadata['process']['total'] = time_process_total

    start_save_image = time()
    out_fp = StringIO()
    result_image.save(out_fp, format='PNG')
    byte_data = out_fp.getvalue()
    stop_save_image = time()
    time_save_image = stop_save_image - start_save_image
    timing_metadata['save'] = time_save_image

    start_b64_encode = time()
    b64_encoded = base64.b64encode(byte_data)
    stop_b64_encode = time()
    time_b64_encode = stop_b64_encode - start_b64_encode
    timing_metadata['b64'] = time_b64_encode

    return b64_encoded, timing_metadata
