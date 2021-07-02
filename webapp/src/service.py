from src.utils import PREDICT_URL
import requests

def predict_from_url(url):
    try:
        response = requests.get(PREDICT_URL, params={'url': url})
        return _handle_response(response)
    except Exception as ex:
        print(ex)
        return {'message': 'could not connect to API'}

def predict_from_file(file):
    try:
        response = requests.post(PREDICT_URL, files={'file': file})
        return _handle_response(response)
    except Exception as ex:
        print(ex)
        return {'message': 'could not connect to API'}

def _handle_response(response):
    try:
        response.raise_for_status()
        return response.json()
    except Exception as ex:
        print(ex)
        return {
            'code': response.status_code,
            'message': 'bad request' if 400 <= response.status_code < 500 else 'error from API'
        }