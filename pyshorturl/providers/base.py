
import requests

from pyshorturl.conf import USER_AGENT_STRING


class ShortenerServiceError(Exception):
    pass


class BaseShortener():
    """Base class for the url shorteners in the lib"""

    def __init__(self, api_key):
        self.headers = {
            'User-Agent': USER_AGENT_STRING,
        }
        self.api_key = api_key

    def _do_http_request(self, request_url, data=None, headers=None):

        if headers:
            self.headers = dict(self.headers.items() + headers.items())

        try:
            if data:
                response = requests.post(request_url, data=data, headers=self.headers)
            else:
                response = requests.get(request_url, headers=self.headers)
            return (response.headers, response.content)

        except requests.exceptions.HTTPError as e:  # pylint: disable=invalid-name
            raise ShortenerServiceError(e)

    def set_api_key(self, api_key):
        self.api_key = api_key

    def shorten_url(self, long_url):
        raise NotImplementedError()

    def expand_url(self, short_url):  # pylint: disable=no-self-use
        response = requests.get(short_url)
        return response.headers.get('location')

    def get_qr_code(self, short_url):
        raise NotImplementedError()

    def write_qr_image(self, short_url, image_path):
        """Obtain the QR code image corresponding to the specified `short_url`
        and write the image to `image_path`.

        If the caller does not intent to use the png image file, `get_qr_code()`
        may be used to obtain raw image data.

        Keyword arguments:
            long_url -- The url to be shortened.

        Returns:
            Returns raw png image data that constitutes the qr code image.

        Exceptions:
            `ShortenerServiceError` - In case of error
        """
        image_data = self.get_qr_code(short_url)

        # pylint: disable=invalid-name
        fd = open(image_path, 'w')
        fd.write(image_data)
        fd.close()
