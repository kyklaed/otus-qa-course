import requests


def get_resp(url):
    response = requests.get(url)
    if response.ok:
        return response
    else:
        return None