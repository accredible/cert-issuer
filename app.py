#!/usr/bin/python3
import json
from flask import Flask, request

from accredible.setup_wallet import setup_wallet
from accredible.setup_logdna import setup_logdna
from accredible.setup_bugsnag import setup_bugsnag
from accredible.setup_configs import parse_configs
from accredible.verifier import verify_signature

import cert_issuer.config
from cert_issuer.blockchain_handlers import ethereum
import cert_issuer.issue_certificates


app = Flask(__name__)
parse_configs()
setup_wallet()
setup_logdna(app)
setup_bugsnag(app)

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
    verify_signature(request)
    config = get_config()
    certificate_batch_handler, transaction_handler, connector = \
            ethereum.instantiate_blockchain_handlers(config, False)
    certificate_batch_handler.set_certificates_in_batch(request.json)

    issue_response = cert_issuer.issue_certificates.issue(
        config,
        certificate_batch_handler,
        transaction_handler
    )

    cost = transaction_handler.tx_cost_constants
    response = {
        "txn_id": issue_response['txid'],
        "gas_price": cost.get_gas_price(),
        "gas_limit": cost.get_gas_limit(),
        "nonce": issue_response['nonce'],
        "receipts": certificate_batch_handler.proof
    }
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
