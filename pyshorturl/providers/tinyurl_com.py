
from urllib.parse import urlencode
from .base import BaseShortener, ShortenerServiceError


TINYURLCOM_SERVICE_URL = "http://tinyurl.com/api-create.php"


class TinyUrlcomError(ShortenerServiceError):
    pass


class TinyUrlcom(BaseShortener):

    exception_class = TinyUrlcomError
    service_url = TINYURLCOM_SERVICE_URL

    def __init__(self, logger=None):
        super().__init__(None, logger=logger)

    def _get_request_url(self):  # pylint: disable=no-self-use
        return self.service_url

    def shorten_url(self, long_url):
        data = {'url': long_url}
        data = urlencode(data)
        request_url = self._get_request_url()
        headers, response = self._do_http_request(request_url, data=data)  # pylint: disable=unused-variable

        if response == 'Error':
            raise self.exception_class('Received Error from tinyurl.com')

        return response
