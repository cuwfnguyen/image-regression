
import json


def load_config(config_file):
    config = load_json(config_file)
    return config

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
