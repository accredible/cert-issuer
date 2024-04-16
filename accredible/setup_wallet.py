import os
import logging


def setup_wallet():
    logging.info('Setting up wallet')

    pk_issuer = os.getenv('WALLET_PRIVATE_KEY')

    with open('./pk_issuer.txt', 'w') as f:
        f.write(pk_issuer)

    os.unsetenv('WALLET_PRIVATE_KEY')
