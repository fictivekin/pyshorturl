
import imghdr
import os
import unittest

from pyshorturl import Googl

class TestGoogl(unittest.TestCase):

    def setUp(self):
        self.test_long_url = 'http://www.parthbhatt.com/blog/'
        self.test_short_url = 'http://goo.gl/RwsEG'
        self.api_key = 'AIzaSyBz_IC5f7AzeG82FyBYWmumO8jZAlXF5WU'
        self.qr_image_path = 'qr.png'

    def tearDown(self):
        if os.path.exists(self.qr_image_path):
            os.unlink(self.qr_image_path)

    def test_shorten_url_with_key(self):
        service = Googl(api_key=self.api_key)
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_write_qr_image(self):
        service = Googl()
        service.write_qr_image(self.test_short_url, self.qr_image_path)

        self.assertEqual('png', imghdr.what(self.qr_image_path))

    def test_expand_url_with_key(self):
        service = Googl(api_key=self.api_key)
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)


if __name__ == '__main__':
    # pylint: disable=invalid-name
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogl)
    unittest.TextTestRunner(verbosity=2).run(suite)
