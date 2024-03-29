import os
import json
import logging

def parse_configs():
    if os.environ['ENV_NAME'] == 'local':
        return

    logging.info('Parsing configs')

    configs_json = os.getenv('CONFIGS')

    configs = json.loads(configs_json)

    for key, value in configs.items():
        os.environ[key] = str(value)