from requests.auth import AuthBase


class Token(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        if self.token:
            r.headers['Authorization'] = 'Bearer {0}'.format(self.token)
        return r
