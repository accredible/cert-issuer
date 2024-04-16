import os
import hmac
import hashlib

from flask import abort


def verify_signature(request):
    x_signature = request.headers.get('X-Signature')

    secret = os.environ.get('SIGNATURE_SECRET')
    payload = os.environ.get('ISSUING_ADDRESS')

    signature = hmac.new(
        bytes(secret, 'utf8'),
        msg=bytes(payload, 'utf8'),
        digestmod=hashlib.sha256
    ).hexdigest()

    if not x_signature or not hmac.compare_digest(x_signature, signature):
        abort(401, 'Unauthorized')
