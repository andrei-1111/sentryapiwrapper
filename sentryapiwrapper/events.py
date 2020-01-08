"""
Contains the methods used for retrieving data from the Sentry API
resource URLs.

docs: https://docs.sentry.io/api/events/
"""

import requests

from . import api


def list_projects():
    """
    Return a list of projects available to the authenticated session.
    """
    url = api.resource_url('projects/')
    r = api.session.get(url)
    return api.return_or_raise(r)

def list_project_events(org_slug, proj_slug):
    """
    Return a list of events bound to a project.
    """
    url = api.resource_url('projects/{org_slug}/{proj_slug}/events/' \
            .format(org_slug=org_slug, proj_slug=proj_slug))
    r = api.session.get(url)
    return api.return_or_raise(r)

def list_project_issues(org_slug, proj_slug):
    """
    Return a list of issues (groups) bound to a project.
    """
    url = api.resource_url('projects/{org_slug}/{proj_slug}/issues/' \
            .format(org_slug=org_slug, proj_slug=proj_slug))
    r = api.session.get(url)
    return api.return_or_raise(r)

def list_issue_events(issue_id):
    """
    This endpoint lists an issue’s events.
    """
    url = api.resource_url('issues/{issue_id}/events/' \
            .format(org_slug=org_slug, proj_slug=proj_slug))
    r = api.session.get(url)
    return api.return_or_raise(r)

def get_issue(issue_id):
    """
    Return details on an individual issue.
    """
    url = api.resource_url('issues/{issue_id}/'.format(
            issue_id=issue_id))
    r = api.session.get(url)
    return api.return_or_raise(r)
