import logging
import math
import sys
import time
from collections import namedtuple
from io import BytesIO
from flask import Blueprint, Flask, current_app, make_response, render_template, request, abort
from flask_caching import Cache
from flask_cors import CORS
from zaloa import (
    generate_coordinates_512,
    generate_coordinates_256,
    generate_coordinates_260,
    generate_coordinates_516,
    is_tile_valid,
    process_tile,
    ImageReducer,
    S3TileFetcher,
    HttpTileFetcher,
    Tile,
)


tile_bp = Blueprint('tiles', __name__)
cache = Cache()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    CORS(app)
    cache.init_app(app)

    @app.before_first_request
    def setup_logging():
        if not app.debug:
            # In production mode, add log handler to sys.stderr.
            app.logger.addHandler(logging.StreamHandler())
            app.logger.setLevel(logging.INFO)

    fetch_type = app.config.get('TILES_FETCH_METHOD')
    assert fetch_type in ('s3', 'http'), "Fetch method must be s3 or http"

    app.register_blueprint(tile_bp)

    return app


@tile_bp.route('/tilezen/terrain/v1/<int:tilesize>/<tileset>/<int:z>/<int:x>/<int:y>.png')
@tile_bp.route('/tilezen/terrain/v1/<tileset>/<int:z>/<int:x>/<int:y>.png')
def handle_tile(z, x, y, tileset, tilesize=None):
    tilesize = tilesize or 256

    if tilesize not in (256, 260, 512, 516):
        return abort(404, 'Invalid tilesize')

    if tileset not in ('terrarium', 'normal'):
        return abort(404, 'Invalid tileset')

    if not is_tile_valid(z, x, y):
        return abort(404, 'Invalid tile coordinate')

    if tilesize != 260 and z == 15:
        return abort(404, 'Invalid zoom')

    tile = Tile(z, x, y)

    image_reducer = ImageReducer(tilesize)

    # both terrarium and normal tiles follow the same
    # coordinate generation strategy. They just point to a
    # different location for the source data
    if tilesize == 512:
        coords_generator = generate_coordinates_512
    elif tilesize == 256:
        coords_generator = generate_coordinates_256
    elif tilesize == 260:
        coords_generator = generate_coordinates_260
    elif tilesize == 516:
        coords_generator = generate_coordinates_516
    else:
        abort(500, 'tileset/tilesize combination unimplemented')

    fetch_type = current_app.config.get('TILES_FETCH_METHOD')
    if fetch_type == 's3':
        import boto3
        bucket = current_app.config.get('TILES_S3_BUCKET')
        s3_client = boto3.client('s3')
        tile_fetcher = S3TileFetcher(s3_client, bucket)
    elif fetch_type == 'http':
        import requests
        url_prefix = current_app.config.get('TILES_HTTP_PREFIX')
        tile_fetcher = HttpTileFetcher(requests, url_prefix)

    image_bytes, timing_metadata, tile_coords = process_tile(
        coords_generator, tile_fetcher, image_reducer, tileset,
        tile)

    resp = make_response(image_bytes)
    resp.content_type = 'image/png'
    return resp


@tile_bp.route('/health_check')
def health_check():
    handle_tile(0, 0, 0, 'terrarium', tilesize=256)
    return 'OK'
