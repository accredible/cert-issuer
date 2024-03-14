import os
import logging
from logdna import LogDNAHandler

key=os.environ['LOGDNA_INGESTION_KEY']

logdna_handler = LogDNAHandler(key, options={
    'app': 'cert-issuer',
})

def setup_logdna():
    logging.getLogger().addHandler(logdna_handler)
