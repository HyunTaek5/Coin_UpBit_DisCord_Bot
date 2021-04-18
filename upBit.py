import hashlib
import time
from urllib.parse import urlencode
import jwt
import requests
import uuid
from core import get_secret

ACCESS_KEY = get_secret("ACCESS_KEY")
SECRET_KEY = get_secret("SECRET_KEY")
payload = {
    'access_key': ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
}


def upbit_balance_check():
    balance = {}
    url = "https://api.upbit.com/v1/accounts"
    jwt_token = jwt.encode(payload, SECRET_KEY)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    response = requests.get(url, headers=headers)
    for i in range(len(response.json())):
        balance[response.json()[i]['currency']] = response.json()[i]['balance']
    return balance


def upbit_get_trade_price(market):
    url = "https://api.upbit.com/v1/candles/days"
    coin, coin_name = get_all_coin()
    if market in coin_name:
        market = coin[market]
    querystring = {"market": market, "count": "1"}
    response = requests.request("GET", url, params=querystring)
    return response.json()[0]['trade_price']


def get_all_coin():
    coin = {}
    coin_name = []
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails": "false"}
    response = requests.request("GET", url, params=querystring)
    for i in range(len(response.json())):
        if 'KRW' in response.json()[i]['market']:
            coin[response.json()[i]['korean_name']] = response.json()[i]['market']
            coin_name.append(response.json()[i]['korean_name'])
    return coin, coin_name

# 테스트용
# get_trade_price("비트코인")
# get_all_coin()
# balance_check()