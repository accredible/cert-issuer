import os
import bugsnag
from bugsnag.flask import handle_exceptions

api_key=os.environ['BUGSNAG_API_KEY']

bugsnag.configure(
    api_key=api_key,
    notify_release_stages=['dev', 'production']
)

def setup_bugsnag(app):
    handle_exceptions(app)
