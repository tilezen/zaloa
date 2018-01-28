import unittest


class CoordsGeneratorTest(unittest.TestCase):

    def test_512(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_512
        tile = Tile(0, 0, 0)
        all_coords = generate_coordinates_512(tile)
        just_tile_coords = [x.tile for x in all_coords]
        exp_coords = [
            Tile(1, 0, 0),
            Tile(1, 1, 0),
            Tile(1, 0, 1),
            Tile(1, 1, 1),
        ]
        self.assertEqual(exp_coords, just_tile_coords)

    def test_260(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 1, 1)
        all_coords = generate_coordinates_260(tile)
        just_tile_coords = [x.tile for x in all_coords]
        exp_coords = [
            Tile(2, 0, 0), Tile(2, 1, 0), Tile(2, 2, 0),
            Tile(2, 0, 1), Tile(2, 1, 1), Tile(2, 2, 1),
            Tile(2, 0, 2), Tile(2, 1, 2), Tile(2, 2, 2),
        ]
        self.assertEqual(exp_coords, just_tile_coords)

    def test_516(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 1, 1)
        all_coords = generate_coordinates_516(tile)
        just_tile_coords = [x.tile for x in all_coords]
        exp_coords = [
            Tile(3, 1, 1), Tile(3, 2, 1), Tile(3, 3, 1), Tile(3, 4, 1),
            Tile(3, 1, 2), Tile(3, 2, 2), Tile(3, 3, 2), Tile(3, 4, 2),
            Tile(3, 1, 3), Tile(3, 2, 3), Tile(3, 3, 3), Tile(3, 4, 3),
            Tile(3, 1, 4), Tile(3, 2, 4), Tile(3, 3, 4), Tile(3, 4, 4),
        ]
        self.assertEqual(exp_coords, just_tile_coords)

    def test_edge_260_topleft(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 0, 0)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(nw.tile, Tile(2, 3, 0))
        self.assertEqual(n.tile, Tile(2, 0, 0))
        self.assertEqual(ne.tile, Tile(2, 1, 0))
        self.assertEqual(w.tile, Tile(2, 3, 0))
        self.assertEqual(c.tile, Tile(2, 0, 0))
        self.assertEqual(e.tile, Tile(2, 1, 0))
        self.assertEqual(nw.image_spec.crop_bounds, (254, 0, 256, 2))
        self.assertEqual(n.image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(ne.image_spec.crop_bounds, (0, 0, 2, 2))

    def test_edge_260_topmid(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 1, 0)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(nw.tile, Tile(2, 0, 0))
        self.assertEqual(n.tile, Tile(2, 1, 0))
        self.assertEqual(ne.tile, Tile(2, 2, 0))
        self.assertEqual(w.tile, Tile(2, 0, 0))
        self.assertEqual(c.tile, Tile(2, 1, 0))
        self.assertEqual(e.tile, Tile(2, 2, 0))
        self.assertEqual(nw.image_spec.crop_bounds, (254, 0, 256, 2))
        self.assertEqual(n.image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(ne.image_spec.crop_bounds, (0, 0, 2, 2))

    def test_edge_260_topright(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 3, 0)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(nw.tile, Tile(2, 2, 0))
        self.assertEqual(n.tile, Tile(2, 3, 0))
        self.assertEqual(ne.tile, Tile(2, 0, 0))
        self.assertEqual(w.tile, Tile(2, 2, 0))
        self.assertEqual(c.tile, Tile(2, 3, 0))
        self.assertEqual(e.tile, Tile(2, 0, 0))
        self.assertEqual(nw.image_spec.crop_bounds, (254, 0, 256, 2))
        self.assertEqual(n.image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(ne.image_spec.crop_bounds, (0, 0, 2, 2))

    def test_edge_260_botleft(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 0, 3)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(sw.tile, Tile(2, 3, 3))
        self.assertEqual(s.tile, Tile(2, 0, 3))
        self.assertEqual(se.tile, Tile(2, 1, 3))
        self.assertEqual(w.tile, Tile(2, 3, 3))
        self.assertEqual(c.tile, Tile(2, 0, 3))
        self.assertEqual(e.tile, Tile(2, 1, 3))
        self.assertEqual(sw.image_spec.crop_bounds, (254, 254, 256, 256))
        self.assertEqual(s.image_spec.crop_bounds, (0, 254, 256, 256))
        self.assertEqual(se.image_spec.crop_bounds, (0, 254, 2, 256))

    def test_edge_260_botmid(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 2, 3)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(sw.tile, Tile(2, 1, 3))
        self.assertEqual(s.tile, Tile(2, 2, 3))
        self.assertEqual(se.tile, Tile(2, 3, 3))
        self.assertEqual(w.tile, Tile(2, 1, 3))
        self.assertEqual(c.tile, Tile(2, 2, 3))
        self.assertEqual(e.tile, Tile(2, 3, 3))
        self.assertEqual(sw.image_spec.crop_bounds, (254, 254, 256, 256))
        self.assertEqual(s.image_spec.crop_bounds, (0, 254, 256, 256))
        self.assertEqual(se.image_spec.crop_bounds, (0, 254, 2, 256))

    def test_edge_260_botright(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 3, 3)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(sw.tile, Tile(2, 2, 3))
        self.assertEqual(s.tile, Tile(2, 3, 3))
        self.assertEqual(se.tile, Tile(2, 0, 3))
        self.assertEqual(w.tile, Tile(2, 2, 3))
        self.assertEqual(c.tile, Tile(2, 3, 3))
        self.assertEqual(e.tile, Tile(2, 0, 3))
        self.assertEqual(sw.image_spec.crop_bounds, (254, 254, 256, 256))
        self.assertEqual(s.image_spec.crop_bounds, (0, 254, 256, 256))
        self.assertEqual(se.image_spec.crop_bounds, (0, 254, 2, 256))

    def test_edge_260_midleft(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 0, 2)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(w.tile, Tile(2, 3, 2))
        self.assertEqual(c.tile, Tile(2, 0, 2))
        self.assertEqual(e.tile, Tile(2, 1, 2))
        self.assertEqual(w.image_spec.crop_bounds, (254, 0, 256, 256))
        self.assertIsNone(c.image_spec.crop_bounds)
        self.assertEqual(e.image_spec.crop_bounds, (0, 0, 2, 256))

    def test_edge_260_midright(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_260
        tile = Tile(2, 3, 1)
        all_coords = generate_coordinates_260(tile)
        nw, n, ne, w, c, e, sw, s, se = all_coords
        self.assertEqual(w.tile, Tile(2, 2, 1))
        self.assertEqual(c.tile, Tile(2, 3, 1))
        self.assertEqual(e.tile, Tile(2, 0, 1))
        self.assertEqual(w.image_spec.crop_bounds, (254, 0, 256, 256))
        self.assertIsNone(c.image_spec.crop_bounds)
        self.assertEqual(e.image_spec.crop_bounds, (0, 0, 2, 256))

    def test_edge_516_topleft(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 0, 0)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[0].tile, Tile(3, 7, 0))
        self.assertEqual(coords[1].tile, Tile(3, 0, 0))
        self.assertEqual(coords[2].tile, Tile(3, 1, 0))
        self.assertEqual(coords[3].tile, Tile(3, 2, 0))
        self.assertEqual(coords[4].tile, Tile(3, 7, 0))
        self.assertEqual(coords[5].tile, Tile(3, 0, 0))
        self.assertEqual(coords[6].tile, Tile(3, 1, 0))
        self.assertEqual(coords[7].tile, Tile(3, 2, 0))
        self.assertEqual(coords[0].image_spec.crop_bounds, (254, 0, 256, 2))
        self.assertEqual(coords[1].image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(coords[2].image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(coords[3].image_spec.crop_bounds, (0, 0, 2, 2))

    def test_edge_516_topmid(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 2, 0)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[0].tile, Tile(3, 3, 0))
        self.assertEqual(coords[1].tile, Tile(3, 4, 0))
        self.assertEqual(coords[2].tile, Tile(3, 5, 0))
        self.assertEqual(coords[3].tile, Tile(3, 6, 0))
        self.assertEqual(coords[4].tile, Tile(3, 3, 0))
        self.assertEqual(coords[5].tile, Tile(3, 4, 0))
        self.assertEqual(coords[6].tile, Tile(3, 5, 0))
        self.assertEqual(coords[7].tile, Tile(3, 6, 0))
        self.assertEqual(coords[0].image_spec.crop_bounds, (254, 0, 256, 2))
        self.assertEqual(coords[1].image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(coords[2].image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(coords[3].image_spec.crop_bounds, (0, 0, 2, 2))

    def test_edge_516_topright(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 3, 0)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[0].tile, Tile(3, 5, 0))
        self.assertEqual(coords[1].tile, Tile(3, 6, 0))
        self.assertEqual(coords[2].tile, Tile(3, 7, 0))
        self.assertEqual(coords[3].tile, Tile(3, 0, 0))
        self.assertEqual(coords[4].tile, Tile(3, 5, 0))
        self.assertEqual(coords[5].tile, Tile(3, 6, 0))
        self.assertEqual(coords[6].tile, Tile(3, 7, 0))
        self.assertEqual(coords[7].tile, Tile(3, 0, 0))
        self.assertEqual(coords[0].tile, Tile(3, 5, 0))
        self.assertEqual(coords[1].tile, Tile(3, 6, 0))
        self.assertEqual(coords[2].tile, Tile(3, 7, 0))
        self.assertEqual(coords[3].tile, Tile(3, 0, 0))
        self.assertEqual(coords[0].image_spec.crop_bounds, (254, 0, 256, 2))
        self.assertEqual(coords[1].image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(coords[2].image_spec.crop_bounds, (0, 0, 256, 2))
        self.assertEqual(coords[3].image_spec.crop_bounds, (0, 0, 2, 2))

    def test_edge_516_midleft(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 0, 3)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[4].tile, Tile(3, 7, 6))
        self.assertEqual(coords[5].tile, Tile(3, 0, 6))
        self.assertEqual(coords[6].tile, Tile(3, 1, 6))
        self.assertEqual(coords[7].tile, Tile(3, 2, 6))
        self.assertEqual(coords[8].tile, Tile(3, 7, 7))
        self.assertEqual(coords[9].tile, Tile(3, 0, 7))
        self.assertEqual(coords[10].tile, Tile(3, 1, 7))
        self.assertEqual(coords[11].tile, Tile(3, 2, 7))
        self.assertEqual(coords[4].image_spec.crop_bounds, (254, 0, 256, 256))
        self.assertEqual(coords[5].image_spec.crop_bounds, None)
        self.assertEqual(coords[6].image_spec.crop_bounds, None)
        self.assertEqual(coords[7].image_spec.crop_bounds, (0, 0, 2, 256))
        self.assertEqual(coords[8].image_spec.crop_bounds, (254, 0, 256, 256))
        self.assertEqual(coords[9].image_spec.crop_bounds, None)
        self.assertEqual(coords[10].image_spec.crop_bounds, None)
        self.assertEqual(coords[11].image_spec.crop_bounds, (0, 0, 2, 256))

    def test_edge_516_midright(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 3, 2)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[4].tile, Tile(3, 5, 4))
        self.assertEqual(coords[5].tile, Tile(3, 6, 4))
        self.assertEqual(coords[6].tile, Tile(3, 7, 4))
        self.assertEqual(coords[7].tile, Tile(3, 0, 4))
        self.assertEqual(coords[8].tile, Tile(3, 5, 5))
        self.assertEqual(coords[9].tile, Tile(3, 6, 5))
        self.assertEqual(coords[10].tile, Tile(3, 7, 5))
        self.assertEqual(coords[11].tile, Tile(3, 0, 5))
        self.assertEqual(coords[4].image_spec.crop_bounds, (254, 0, 256, 256))
        self.assertEqual(coords[5].image_spec.crop_bounds, None)
        self.assertEqual(coords[6].image_spec.crop_bounds, None)
        self.assertEqual(coords[7].image_spec.crop_bounds, (0, 0, 2, 256))
        self.assertEqual(coords[8].image_spec.crop_bounds, (254, 0, 256, 256))
        self.assertEqual(coords[9].image_spec.crop_bounds, None)
        self.assertEqual(coords[10].image_spec.crop_bounds, None)
        self.assertEqual(coords[11].image_spec.crop_bounds, (0, 0, 2, 256))

    def test_edge_516_botleft(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 0, 3)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[8].tile, Tile(3, 7, 7))
        self.assertEqual(coords[9].tile, Tile(3, 0, 7))
        self.assertEqual(coords[10].tile, Tile(3, 1, 7))
        self.assertEqual(coords[11].tile, Tile(3, 2, 7))
        self.assertEqual(coords[12].tile, Tile(3, 7, 7))
        self.assertEqual(coords[13].tile, Tile(3, 0, 7))
        self.assertEqual(coords[14].tile, Tile(3, 1, 7))
        self.assertEqual(coords[15].tile, Tile(3, 2, 7))
        self.assertEqual(coords[12].image_spec.crop_bounds,
                          (254, 254, 256, 256))
        self.assertEqual(coords[13].image_spec.crop_bounds,
                          (0, 254, 256, 256))
        self.assertEqual(coords[14].image_spec.crop_bounds,
                          (0, 254, 256, 256))
        self.assertEqual(coords[15].image_spec.crop_bounds,
                          (0, 254, 2, 256))

    def test_edge_516_botmid(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 1, 3)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[8].tile, Tile(3, 1, 7))
        self.assertEqual(coords[9].tile, Tile(3, 2, 7))
        self.assertEqual(coords[10].tile, Tile(3, 3, 7))
        self.assertEqual(coords[11].tile, Tile(3, 4, 7))
        self.assertEqual(coords[12].tile, Tile(3, 1, 7))
        self.assertEqual(coords[13].tile, Tile(3, 2, 7))
        self.assertEqual(coords[14].tile, Tile(3, 3, 7))
        self.assertEqual(coords[15].tile, Tile(3, 4, 7))
        self.assertEqual(coords[12].image_spec.crop_bounds,
                          (254, 254, 256, 256))
        self.assertEqual(coords[13].image_spec.crop_bounds,
                          (0, 254, 256, 256))
        self.assertEqual(coords[14].image_spec.crop_bounds,
                          (0, 254, 256, 256))
        self.assertEqual(coords[15].image_spec.crop_bounds,
                          (0, 254, 2, 256))

    def test_edge_516_botright(self):
        from zaloa import Tile
        from zaloa import generate_coordinates_516
        tile = Tile(2, 3, 3)
        coords = generate_coordinates_516(tile)
        self.assertEqual(coords[8].tile, Tile(3, 5, 7))
        self.assertEqual(coords[9].tile, Tile(3, 6, 7))
        self.assertEqual(coords[10].tile, Tile(3, 7, 7))
        self.assertEqual(coords[11].tile, Tile(3, 0, 7))
        self.assertEqual(coords[12].tile, Tile(3, 5, 7))
        self.assertEqual(coords[13].tile, Tile(3, 6, 7))
        self.assertEqual(coords[14].tile, Tile(3, 7, 7))
        self.assertEqual(coords[15].tile, Tile(3, 0, 7))
        self.assertEqual(coords[12].image_spec.crop_bounds,
                          (254, 254, 256, 256))
        self.assertEqual(coords[13].image_spec.crop_bounds,
                          (0, 254, 256, 256))
        self.assertEqual(coords[14].image_spec.crop_bounds,
                          (0, 254, 256, 256))
        self.assertEqual(coords[15].image_spec.crop_bounds,
                          (0, 254, 2, 256))


class S3FetchTest(unittest.TestCase):

    def test_success(self):

        class StubS3Client(object):

            def get_object(self, **kwargs):
                self.kwargs = kwargs
                from io import BytesIO
                return dict(
                    Body=BytesIO(b'image data'),
                )

        from zaloa import S3TileFetcher
        bucket = 'fake-bucket'
        from zaloa import Tileset
        tileset = Tileset.terrarium
        stub_s3_client = StubS3Client()
        s3_tile_fetcher = S3TileFetcher(stub_s3_client, bucket)
        from zaloa import Tile
        fetch_result = s3_tile_fetcher(tileset, Tile(3, 2, 1))
        self.assertEqual(b'image data', fetch_result.image_bytes)
        self.assertEqual('fake-bucket', stub_s3_client.kwargs['Bucket'])
        self.assertEqual('terrarium/3/2/1.png', stub_s3_client.kwargs['Key'])

    def test_missing(self):

        class StubS3Exception(Exception):

            def __init__(self, *args, **kwargs):
                super(StubS3Exception, self).__init__(*args, **kwargs)
                self.response = dict(
                    Error=dict(
                        Code='NoSuchKey',
                    ),
                )

        class StubS3Client(object):

            def get_object(self, **kwargs):
                raise StubS3Exception('test missing tile')

        from zaloa import S3TileFetcher
        bucket = 'fake-bucket'
        from zaloa import Tileset
        tileset = Tileset.terrarium
        stub_s3_client = StubS3Client()
        s3_tile_fetcher = S3TileFetcher(stub_s3_client, bucket)
        from zaloa import Tile
        from zaloa import MissingTileException
        with self.assertRaises(MissingTileException) as cm:
            s3_tile_fetcher(tileset, Tile(3, 2, 1))
        self.assertEqual(Tile(3, 2, 1), cm.exception.tile)

    def test_unknown_exception(self):

        class StubS3Exception(Exception):
            pass

        class StubS3Client(object):

            def get_object(self, **kwargs):
                raise StubS3Exception('unknown exception')

        from zaloa import S3TileFetcher
        bucket = 'fake-bucket'
        from zaloa import Tileset
        tileset = Tileset.terrarium
        stub_s3_client = StubS3Client()
        s3_tile_fetcher = S3TileFetcher(stub_s3_client, bucket)
        from zaloa import Tile
        from zaloa import MissingTileException
        with self.assertRaises(Exception) as cm:
            s3_tile_fetcher(tileset, Tile(3, 2, 1))
        self.assertFalse(isinstance(cm.exception, MissingTileException))
        self.assertEqual('unknown exception', cm.exception.args[0])


class HttpFetchTest(unittest.TestCase):

    def test_success(self):

        class StubHttpResponse(object):

            def __init__(self, status_code, content):
                self.status_code = status_code
                self.content = content

        class StubHttpClient(object):

            def get(self, url):
                self.url = url
                return StubHttpResponse(200, 'image data')

        from zaloa import HttpTileFetcher
        from zaloa import Tileset
        tileset = Tileset.terrarium
        stub_http_client = StubHttpClient()
        url_prefix = 'http://foo'
        http_tile_fetcher = HttpTileFetcher(stub_http_client, url_prefix)
        from zaloa import Tile
        fetch_result = http_tile_fetcher(tileset, Tile(3, 2, 1))
        self.assertEqual('image data', fetch_result.image_bytes)
        self.assertEqual(
            'http://foo/terrarium/3/2/1.png', stub_http_client.url)

    def test_missing(self):

        class StubHttpResponse(object):

            def __init__(self, status_code):
                self.status_code = status_code

        class StubHttpClient(object):

            def get(self, url):
                return StubHttpResponse(404)

        from zaloa import HttpTileFetcher
        from zaloa import Tileset
        tileset = Tileset.terrarium
        stub_http_client = StubHttpClient()
        url_prefix = 'http://foo'
        http_tile_fetcher = HttpTileFetcher(stub_http_client, url_prefix)
        from zaloa import Tile
        from zaloa import MissingTileException
        with self.assertRaises(MissingTileException) as cm:
            http_tile_fetcher(tileset, Tile(3, 2, 1))
        self.assertEqual(Tile(3, 2, 1), cm.exception.tile)

    def test_unknown_exception(self):

        class StubHttpException(Exception):
            pass

        class StubHttpClient(object):

            def get(self, url):
                raise StubHttpException('unknown exception')

        from zaloa import HttpTileFetcher
        from zaloa import Tileset
        tileset = Tileset.terrarium
        stub_http_client = StubHttpClient()
        url_prefix = 'http://foo'
        http_tile_fetcher = HttpTileFetcher(stub_http_client, url_prefix)
        from zaloa import Tile
        from zaloa import MissingTileException
        with self.assertRaises(Exception) as cm:
            http_tile_fetcher(tileset, Tile(3, 2, 1))
        self.assertFalse(isinstance(cm.exception, MissingTileException))
        self.assertEqual('unknown exception', cm.exception.args[0])


class ProcessTileTest(unittest.TestCase):

    def test_basic_invocation(self):
        from zaloa import process_tile
        from zaloa import generate_coordinates_512
        from zaloa import Tile
        from zaloa import Tileset

        def stub_fetch(tileset, tile):
            from zaloa import FetchResult
            return FetchResult('image data', tile)

        class StubImageReducer(object):

            def create_initial_state(self):
                return None

            def reduce(self, image_state, image_input):
                pass

            def finalize(self, image_state):
                return 'combined image data'

        stub_reducer = StubImageReducer()

        response, metadata, tiles = process_tile(
            generate_coordinates_512,
            stub_fetch,
            stub_reducer,
            Tileset.terrarium,
            Tile(0, 0, 0),
        )

        self.assertEqual('combined image data', response)

    def _gen_stub_image(self, color):
        from PIL import Image
        im = Image.new('RGB', (256, 256))
        for y in range(256):
            for x in range(256):
                im.putpixel((x, y), color)
        from io import BytesIO
        fp = BytesIO()
        im.save(fp, format='PNG')
        return fp.getvalue()

    def test_validity_512(self):
        from zaloa import process_tile
        from zaloa import generate_coordinates_512
        from zaloa import Tile
        from zaloa import Tileset

        def stub_fetch(tileset, tile):
            # return back
            # r g
            # b w
            # oriented around test coordinate of 2/1/1
            from zaloa import FetchResult
            if tile == Tile(3, 2, 2):
                # nw
                color = 255, 0, 0
            elif tile == Tile(3, 3, 2):
                # ne
                color = 0, 255, 0
            elif tile == Tile(3, 2, 3):
                # sw
                color = 0, 0, 255
            elif tile == Tile(3, 3, 3):
                # se
                color = 255, 255, 255
            else:
                assert not 'Invalid tile coordinate: %s' % tile
            image_bytes = self._gen_stub_image(color)
            return FetchResult(image_bytes, tile)

        from zaloa import ImageReducer
        image_reducer = ImageReducer(512)

        image_bytes, metadata, tiles = process_tile(
            generate_coordinates_512,
            stub_fetch,
            image_reducer,
            Tileset.terrarium,
            Tile(2, 1, 1),
        )

        from io import BytesIO
        fp = BytesIO(image_bytes)
        from PIL import Image
        im = Image.open(fp)

        # nw -> red
        # ne -> green
        # sw -> blue
        # se -> white
        expectations = (
            ((0, 0, 256, 256), (255, 0, 0, 255)),
            ((256, 0, 512, 256), (0, 255, 0, 255)),
            ((0, 256, 256, 512), (0, 0, 255, 255)),
            ((256, 256, 512, 512), (255, 255, 255, 255)),
        )
        for region_bounds, color in expectations:
            for y in range(region_bounds[1], region_bounds[3]):
                for x in range(region_bounds[0], region_bounds[2]):
                    pixel = im.getpixel((x, y))
                    self.assertEqual(color, pixel)

    def test_validity_260(self):
        from zaloa import process_tile
        from zaloa import generate_coordinates_260
        from zaloa import Tile
        from zaloa import Tileset

        def stub_fetch(tileset, tile):
            # return back
            # r r r
            # g w g
            # b b b
            # oriented around test coordinate of 2/1/1
            from zaloa import FetchResult
            if tile in (Tile(2, 0, 0), Tile(2, 1, 0), Tile(2, 2, 0)):
                # top row
                color = 255, 0, 0
            elif tile in (Tile(2, 0, 1), Tile(2, 2, 1)):
                # left and right edges
                color = 0, 255, 0
            elif tile == Tile(2, 1, 1):
                # center tile
                color = 255, 255, 255
            elif tile in (Tile(2, 0, 2), Tile(2, 1, 2), Tile(2, 2, 2)):
                # bottom row
                color = 0, 0, 255
            else:
                assert not 'Invalid tile coordinate: %s' % tile
            image_bytes = self._gen_stub_image(color)
            return FetchResult(image_bytes, tile)

        from zaloa import ImageReducer
        image_reducer = ImageReducer(260)

        image_bytes, metadata, tiles = process_tile(
            generate_coordinates_260,
            stub_fetch,
            image_reducer,
            Tileset.terrarium,
            Tile(2, 1, 1),
        )

        from io import BytesIO
        fp = BytesIO(image_bytes)
        from PIL import Image
        im = Image.open(fp)

        # top 2 rows should be red
        # left and right 2 columns should be green
        # center should be white
        # bottom 2 rows should be blue
        expectations = (
            # top rows red
            ((0, 0, 260, 2), (255, 0, 0, 255)),

            # left cols green
            ((0, 2, 2, 258), (0, 255, 0, 255)),
            # right cols green
            ((258, 2, 260, 258), (0, 255, 0, 255)),

            # center white
            ((2, 2, 258, 258), (255, 255, 255, 255)),

            # bottom rows blue
            ((0, 258, 260, 260), (0, 0, 255, 255)),
        )
        for region_bounds, color in expectations:
            for y in range(region_bounds[1], region_bounds[3]):
                for x in range(region_bounds[0], region_bounds[2]):
                    pixel = im.getpixel((x, y))
                    self.assertEqual(color, pixel)

    def test_validity_516(self):
        from zaloa import process_tile
        from zaloa import generate_coordinates_516
        from zaloa import Tile
        from zaloa import Tileset

        def stub_fetch(tileset, tile):
            from zaloa import FetchResult

            # return back
            # r r r r
            # g w w g
            # g w w g
            # b b b b

            # oriented around test coordinate of 2/1/1
            # 2/1/1 -> 3/2/2 (top left corner)

            # 3/1/1 3/2/1 3/3/1 3/4/1
            # 3/1/2 3/2/2 3/3/2 3/4/2
            # 3/1/3 3/2/3 3/3/3 3/4/3
            # 3/1/4 3/2/4 3/3/4 3/4/4

            if tile in (Tile(3, 1, 1), Tile(3, 2, 1),
                        Tile(3, 3, 1), Tile(3, 4, 1)):
                # top row
                color = 255, 0, 0
            elif tile in (Tile(3, 1, 2), Tile(3, 1, 3),
                          Tile(3, 4, 2), Tile(3, 4, 3)):
                # left and right edges
                color = 0, 255, 0
            elif tile in (Tile(3, 2, 2), Tile(3, 3, 2),
                          Tile(3, 2, 3), Tile(3, 3, 3)):
                # center tiles
                color = 255, 255, 255
            elif tile in (Tile(3, 1, 4), Tile(3, 2, 4),
                          Tile(3, 3, 4), Tile(3, 4, 4)):
                # bottom row
                color = 0, 0, 255
            else:
                assert not 'Invalid tile coordinate: %s' % tile
            image_bytes = self._gen_stub_image(color)
            return FetchResult(image_bytes, tile)

        from zaloa import ImageReducer
        image_reducer = ImageReducer(516)

        image_bytes, metadata, tiles = process_tile(
            generate_coordinates_516,
            stub_fetch,
            image_reducer,
            Tileset.terrarium,
            Tile(2, 1, 1),
        )

        from io import BytesIO
        fp = BytesIO(image_bytes)
        from PIL import Image
        im = Image.open(fp)

        # top 2 rows should be red
        # left and right 2 columns should be green
        # center should be white
        # bottom 2 rows should be blue
        expectations = (
            # top rows red
            ((0, 0, 516, 2), (255, 0, 0, 255)),

            # left cols green
            ((0, 2, 2, 514), (0, 255, 0, 255)),
            # right cols green
            ((514, 2, 516, 514), (0, 255, 0, 255)),

            # center white
            ((2, 2, 514, 514), (255, 255, 255, 255)),

            # bottom rows blue
            ((0, 514, 516, 516), (0, 0, 255, 255)),
        )
        for region_bounds, color in expectations:
            for y in range(region_bounds[1], region_bounds[3]):
                for x in range(region_bounds[0], region_bounds[2]):
                    pixel = im.getpixel((x, y))
                    self.assertEqual(color, pixel)


if __name__ == '__main__':
    unittest.main()
