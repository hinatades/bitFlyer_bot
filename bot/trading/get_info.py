
# -*- coding: utf-8 -*-

import json
import requests
import time
import hmac
import hashlib

from key import API_KEY, SECRET_KEY

api_endpoint = 'https://api.bitflyer.jp'

def get_info(path):
    method = 'GET'
    api_endpoint = 'https://api.bitflyer.jp'
    timestamp = str(time.time())
    text = timestamp + method + path
    sign = hmac.new(SECRET_KEY.encode(), text.encode(), hashlib.sha256).hexdigest()
    res = requests.get(
        api_endpoint + '/v1/' + path,
        headers = {
            'ACCESS-KEY': API_KEY,
            'ACCESS-TIMESTAMP': timestamp,
            'ACCESS-SIGN': sign,
            'Content-Type': 'application/json'
        })
    return res.json()    
