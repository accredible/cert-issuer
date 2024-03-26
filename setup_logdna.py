import os
import logging
from logdna import LogDNAHandler


def setup_logdna(app):
    if os.environ['FLASK_ENV'] == 'local':
        return

    key=os.environ['LOGDNA_INGESTION_KEY']

    logdna_handler = LogDNAHandler(key, options={
        'app': 'cert-issuer',
        'env': os.environ['FLASK_ENV']
    })

    app.logger.addHandler(logdna_handler)
    logging.getLogger().addHandler(logdna_handler)
