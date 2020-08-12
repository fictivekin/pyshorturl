
import logging
import requests

from pyshorturl.conf import USER_AGENT_STRING


LOGGER = logging.getLogger('pyshorturl.shortener')


class ShortenerServiceError(Exception):
    pass


class BaseShortener():
    """Base class for the url shorteners in the lib"""

    exception_class = ShortenerServiceError
    service_url = None

    def __init__(self, api_key, *, logger=None):
        self.headers = {
            'User-Agent': USER_AGENT_STRING,
        }
        self.api_key = api_key
        self.logger = logger if logger else LOGGER

    def _do_http_request(self, request_url, *, json=None, data=None, headers=None):

        if not self.service_url:
            raise self.exception_class('Service URL is empty. Cannot proceed with URL shortening.')

        if headers:
            self.headers.update(headers)

        try:
            if data or json:
                self.logger.debug('Sending POST request to %s' % request_url)
                self.logger.debug('Headers: %s' % self.headers)
                self.logger.debug('Data: %s' % data)
                self.logger.debug('JSON: %s' % json)
                response = requests.post(request_url, json=json, data=data, headers=self.headers)

            else:
                self.logger.debug('Sending GET request to %s' % request_url)
                self.logger.debug('Headers: %s' % self.headers)
                response = requests.get(request_url, headers=self.headers)

            response.raise_for_status()
            if response.headers.get('Content-Type') == 'application/json':
                return (response.headers, response.json())
            return (response.headers, response.content)

        except requests.exceptions.HTTPError as e:  # pylint: disable=invalid-name
            raise self.exception_class(e)

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
