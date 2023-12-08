import requests
import os

def get_token(user, password):
    base_url = "https://keycloak.auth.apoorva64.com/realms/nuit-info-2023/protocol/openid-connect/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    the_data = {
        "client_id": "nuit-info",
        "grant_type": "password",
        "client_secret": "XrN3RHGwXCAZtYmEgYVMw1Dj4JWY74mi",
        "scope": "openid",
        "username": user,
        "password": password
    }
    resp = requests.post(base_url, data=the_data, headers=headers)
    data = resp.json()
    return data["access_token"]