
import json

from .base import BaseShortener, ShortenerServiceError


GOOGL_SERVICE_URL = 'https://www.googleapis.com/urlshortener/v1/url'


class GooglError(ShortenerServiceError):
    pass


class Googl(BaseShortener):
    def __init__(self, api_key=None):
        BaseShortener.__init__(self, api_key)
        # goo.gl mandates that requests containing JSON content bodies must be
        # accompanied by a "Content-Type: application/json" request header.
        # Otherwise, the request will result in an Error (400: Bad Request).
        self.headers['Content-Type'] = 'application/json'

    def _get_request_url(self, url_params={}):  # pylint: disable=dangerous-default-value
        request_url = GOOGL_SERVICE_URL
        param_list = []

        if self.api_key:
            param_list.append('key=%s' %self.api_key)

        for param in url_params.keys():
            param_list.append('%s=%s' %(param, url_params.get(param)))
        params = '&'.join(param_list)

        if params:
            request_url = request_url + '?' + params

        return request_url

    def shorten_url(self, long_url):
        data = """{"longUrl": "%s"}""" %long_url

        request_url = self._get_request_url()
        headers, response = self._do_http_request(request_url, data)  # pylint: disable=unused-variable

        response = json.loads(response)
        return response.get('id')

    def expand_url(self, short_url):
        url_params = {'shortUrl':short_url}
        request_url = self._get_request_url(url_params)

        headers, response = self._do_http_request(request_url)  # pylint: disable=unused-variable
        response = json.loads(response)

        status = response.get('status')
        if status == 'REMOVED':
            raise GooglError(
                'Unable to obtain long url for %s. The url status is REMOVED.' % short_url)
        elif status == 'OK':
            response = response.get('longUrl')

        return response

    def get_qr_code(self, short_url):
        qr_url = short_url + '.qr'
        headers, response = self._do_http_request(qr_url)  # pylint: disable=unused-variable

        return response
