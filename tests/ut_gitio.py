
import unittest

from pyshorturl import Gitio

class TestGitio(unittest.TestCase):

    def setUp(self):
        self.test_long_url = 'https://github.com/blog/985-git-io-github-url-shortener'
        self.test_short_url = 'https://git.io/PUikkQ' # self.test_long_url shortens to this.

    def test_shorten_url(self):
        service = Gitio()
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_expand_url(self):
        service = Gitio()
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)


if __name__ == '__main__':
    # pylint: disable=invalid-name
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGitio)
    unittest.TextTestRunner(verbosity=2).run(suite)
