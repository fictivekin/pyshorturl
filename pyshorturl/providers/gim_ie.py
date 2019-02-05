
import requests

from .base import BaseShortener, ShortenerServiceError


GIMIE_SERVICE_URL = "https://gim.ie"


class GimieError(ShortenerServiceError):
    pass


class Gimie(BaseShortener):

    def __init__(self, api_key=None):
        BaseShortener.__init__(self, api_key=api_key)

    def _get_request_url(self):  # pylint: disable=no-self-use
        return '/'.join((GIMIE_SERVICE_URL, 'shorten-me'))

    def shorten_url(self, long_url):
        data = {'url': long_url}
        request_url = self._get_request_url()
        headers = {
            'Authorization': 'Bearer {}'.format(self.api_key)
        }

        try:
            headers, response = self._do_http_request(request_url, data, headers)
        except Exception as e:  # pylint: disable=invalid-name
            raise GimieError('Received Error from gim.ie', e)

        if not response:
            raise GimieError('Received Error from gim.ie')

        return '/'.join((GIMIE_SERVICE_URL, response['code']))

    def _do_http_request(self, request_url, data=None, headers=None):

        if headers:
            self.headers.update(headers.items())

        if data:
            response = requests.post(request_url, json=data, headers=self.headers)
        else:
            response = requests.get(request_url, headers=self.headers)

        return (response.headers, response.json())
