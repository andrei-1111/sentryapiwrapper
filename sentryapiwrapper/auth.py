
import requests


class SentryAuth(requests.auth.AuthBase):
    """
    This class provides the required headers used to make an authenticated
    request.  The `AuthBase` object can be used on multiple requests.

    docs: https://2.python-requests.org//en/master/user/authentication/#new-forms-of-authentication
    """

    def __init__(self, token=None):
        self.token = token

    def __call__(self, r):
        """
        Set an authorization header with the required token string format
        from Sentry.
        """
        r.headers['authorization'] = 'Bearer {}'.format(self.token)
        return r
