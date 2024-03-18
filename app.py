#!/usr/bin/python3
import json
from flask import Flask, request

from logdna_config import setup_logdna
from bugsnag_config import setup_bugsnag

import cert_issuer.config
from cert_issuer.blockchain_handlers import ethereum
import cert_issuer.issue_certificates


app = Flask(__name__)
setup_bugsnag(app)
setup_logdna()

config = None

def get_config():
    global config
    if config == None:
        config = cert_issuer.config.get_config()
    return config

@app.route('/')
def home():
    return 'Certificate Issuance Service is running.'

@app.route('/hc')
def aws_healthcheck():
    return 'OK'

@app.route('/cert_issuer/api/v1.0/issue', methods=['POST'])
def issue():
    config = get_config()
    certificate_batch_handler, transaction_handler, connector = \
            ethereum.instantiate_blockchain_handlers(config, False)
    certificate_batch_handler.set_certificates_in_batch(request.json)
    issue_response = cert_issuer.issue_certificates.issue(config, certificate_batch_handler, transaction_handler)
    response = {
        "txn_id": issue_response['txid'],
        "nonce": issue_response['nonce'],
        "receipts": certificate_batch_handler.proof
    }
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
