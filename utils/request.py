import requests

def get_auth_request(token, url):
    headers = {"Authorization": "Bearer " + token}
    return requests.get(url, headers=headers).json()

def post_auth_request(token, url, data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    return requests.post(url, json=data, headers=headers).json()