import os
import logging
from logdna import LogDNAHandler


def setup_logdna(app):
    if os.environ['ENV_NAME'] == 'local':
        return

    logging.info('Setting up LogDNA')

    key=os.environ['LOGDNA_INGESTION_KEY']

    logdna_handler = LogDNAHandler(key, options={
        'app': 'cert-issuer',
        'env': os.environ['ENV_NAME']
    })

    app.logger.addHandler(logdna_handler)
    logging.getLogger().addHandler(logdna_handler)
