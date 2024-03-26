import os
import json

def parse_configs():
    configs_json = os.getenv('CONFIGS')

    configs = json.loads(configs_json)

    for key, value in configs.items():
        os.environ[key] = str(value)
