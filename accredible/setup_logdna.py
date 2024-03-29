import os
import logging
from logdna import LogDNAHandler


def setup_logdna(app):
    env = os.environ.get('ENV_NAME')

    if env == 'local':
        return

    logging.info('Setting up LogDNA')

    key=os.environ['LOGDNA_INGESTION_KEY']

    logdna_handler = LogDNAHandler(key, options={
        'app': 'cert-issuer',
        'env': env,
        'tags': [env],
    })

    app.logger.addHandler(logdna_handler)
    logging.getLogger().addHandler(logdna_handler)
