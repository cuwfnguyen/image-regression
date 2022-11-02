import json


def load_samples(samples_file):
    return load_json(samples_file)

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
