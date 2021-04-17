import os
import json

secret_file = os.path.join('secrets.json')
with open(secret_file) as f:
    secret = json.loads(f.read())


def get_secret(setting, secrets=secret):
    try:
        return secrets[setting]
    except KeyError:
        print('error!')