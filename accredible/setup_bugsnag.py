import os
import logging
import bugsnag
from bugsnag.flask import handle_exceptions


def setup_bugsnag(app):
    if os.environ['ENV_NAME'] == 'local':
        return

    logging.info('Setting up Bugsnag')

    api_key=os.environ['BUGSNAG_API_KEY']

    bugsnag.configure(
        api_key=api_key,
        project_root='/cert-issuer',
        release_stage=os.environ['ENV_NAME'],
        notify_release_stages=['dev', 'production']
    )

    handle_exceptions(app)
