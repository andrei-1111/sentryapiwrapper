
import os
import requests
import urllib.parse

from .auth import SentryAuth


SENTRY_API_TOKEN = os.environ.get('SENTRY_API_TOKEN', None)
SENTRY_URL = 'https://sentry.io/api/0/'


class TokenNotFound(Exception):
    pass


class SentryAPI(object):
    """ A client for interacting with the Sentry API. """

    def __init__(self, base_uri=None, token=None):
        self.base_uri = base_uri

        if not SENTRY_API_TOKEN:
            raise TokenNotFound('Sentry API Token is required.')

        self.auth = SentryAuth(token=token)

        self.session = requests.Session()
        self.session.auth = self.auth

    def resource_url(self, path):
        """ Generate a resource URL based from a given path. """
        return urllib.parse.urljoin(self.base_uri, path)

    def return_or_raise(self, response):
        """
        Returns the JSON format of the reponse if the request succeeds.
        Otherwise, it raises an exception.
        """
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()


# Default API connection that will auth the first time it is used.
api = SentryAPI(base_uri=SENTRY_URL, token=SENTRY_API_TOKEN)
