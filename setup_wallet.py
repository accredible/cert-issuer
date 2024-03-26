import os


def setup_wallet():
    pk_issuer = os.environ.get('WALLET_PRIVATE_KEY')

    with open('./pk_issuer.txt', 'w') as f:
        f.write(pk_issuer)
