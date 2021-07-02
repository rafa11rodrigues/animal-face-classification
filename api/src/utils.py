import pickle
import yaml
from PIL import Image
import requests

_model = None

def _load_config(config_path='config.yaml'):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_pickle_file(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def load_model():
    global _model
    if _model is None:
        config = _load_config()
        path_to_model = f'{config["models"]["base_path"]}/{config["models"]["selected_model"]}.pkl'
        _model = load_pickle_file(path_to_model)
    return _model

def load_image_from_url(url):
    return Image.open(requests.get(url, stream=True).raw)

def load_image_from_bytes(bytes):
    return Image.open(bytes)