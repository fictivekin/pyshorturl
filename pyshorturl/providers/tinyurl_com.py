
from urllib.parse import urlencode
from .base import BaseShortener, ShortenerServiceError


TINYURLCOM_SERVICE_URL = "http://tinyurl.com/api-create.php"


class TinyUrlcomError(ShortenerServiceError):
    pass


class TinyUrlcom(BaseShortener):

    def __init__(self):
        BaseShortener.__init__(self, api_key=None)

    def _get_request_url(self):  # pylint: disable=no-self-use
        return TINYURLCOM_SERVICE_URL

    def shorten_url(self, long_url):
        data = {'url': long_url}
        data = urlencode(data)
        request_url = self._get_request_url()
        headers, response = self._do_http_request(request_url, data)  # pylint: disable=unused-variable

        if response == 'Error':
            raise TinyUrlcomError('Received Error from tinyurl.com')

        return response
