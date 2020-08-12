
import requests

from .base import BaseShortener, ShortenerServiceError


GIMME_BAR_SERVICE_URL = "https://gimme.bar"


class GimmeBarError(ShortenerServiceError):
    pass


class GimmeBar(BaseShortener):

    exception_class = GimmeBarError
    service_url = GIMME_BAR_SERVICE_URL

    def __init__(self, api_key=None, logger=None):
        super().__init__(api_key=api_key, logger=logger)

    def _get_request_url(self):  # pylint: disable=no-self-use
        return '/'.join((self.service_url, 'shorten-me'))

    def shorten_url(self, long_url):
        data = {'url': long_url}
        request_url = self._get_request_url()
        headers = {
            'Authorization': 'Bearer {}'.format(self.api_key)
        }

        try:
            headers, response = self._do_http_request(request_url, json=data, headers=headers)
        except Exception as e:  # pylint: disable=invalid-name
            raise self.exception_class('Received Error from gim.ie', e)

        if not response:
            raise self.exception_class('Received empty response from gim.ie')

        self.logger.debug(response)
        return '/'.join((self.service_url, response['code']))
