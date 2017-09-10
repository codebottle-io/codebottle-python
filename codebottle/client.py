import requests

from .exceptions import CodebottleError
from .auth import Token


class Result(object):
    '''A class with attributes of a codebottle API result'''
    def __init__(self, r):
        self.json = r.json()
        if self.json.get('error'):
            raise CodebottleError(self.json['error'])

        for k, v in self.json.items():
            setattr(self, k, v)


class CodeBottle(object):

    def __init__(self, token=None):
        self.api_url = 'https://api.codebottle.io'
        self.api_accept = 'application/vnd.codebottle.v1+json'
        self.token = token

    def _build_url(self, endpoint, *args):
        url = '{0}/{1}'.format(self.api_url, endpoint)
        if len(args) > 0:
            args = [str(a) for a in args]
            url = '{0}/{1}'.format(url, '/'.join(args))
        return url

    def _get(self, endpoint, *args, **kwargs):
        url = self._build_url(endpoint, *args)
        r = requests.get(url, params=kwargs, auth=Token(self.token),
                         headers={'Accept': self.api_accept})
        return Result(r)

    def _post(self, endpoint, *args, **kwargs):
        url = self._build_url(endpoint, *args)
        r = requests.post(url, data=kwargs, auth=Token(self.token),
                          headers={'Accept': self.api_accept})
        return Result(r)

    def languages(self, *args):
        return self._get('languages', *args)

    def categories(self, *args):
        return self._get('categories', *args)

    def snippets(self, *args, **kwargs):
        return self._get('snippets', *args, **kwargs)

    def create_snippet(self, **kwargs):
        return self._post('snippets', **kwargs)

    def vote(self, *args, **kwargs):
        return self._post('snippets', *args, **kwargs)
