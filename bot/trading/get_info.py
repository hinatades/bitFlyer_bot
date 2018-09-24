
# -*- coding: utf-8 -*-

import json
import requests
import time
import hmac
import hashlib
from pytz import timezone
from time import sleep
from datetime import datetime
from key import USER_NAME, API_KEY, SECRET_KEY, SLACK_URL


def get_info(path, query_params=None):
    method = 'GET'
    api_endpoint = 'https://api.bitflyer.jp'
    timestamp = str(time.time())
    text = timestamp + method + path # + body
    sign = hmac.new(SECRET_KEY.encode(), text.encode(), hashlib.sha256).hexdigest()
    res = requests.get(
        api_endpoint + path,
        headers = {
            'ACCESS-KEY': API_KEY,
            'ACCESS-TIMESTAMP': timestamp,
            'ACCESS-SIGN': sign,
            'Content-Type': 'application/json'
        })
    return res.json()


def post_notification(info):
    """
    Post notification to #dev
    """
    api_endpoint = SLACK_URL
    requests.post(
        api_endpoint,
        data=json.dumps({"text": str(_process_json_array(USER_NAME, info))})
    )


def _process_json_array(user, json_array):

    new_list = []
    for i in json_array:
        new_dict = {'user': user}
        for k, v in i.items():
            if k == 'size':
                new_dict['枚数'] = v
            elif k == 'child_order_date':
                try:
                    dt = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    jst_time = dt.astimezone(timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
                except ValueError:
                    dt = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
                    jst_time = dt.astimezone(timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
                new_dict['注文時刻'] = jst_time
            elif k == 'side':
                 new_dict['注文'] = v
        new_list.append(new_dict)
    return new_list


def build_local_bot():
    """
    """
    num = 0
    res = []
    befor_order_time = ''
    while (num < 5):
        sleep(1)
        res = get_info('/v1/me/getchildorders?product_code=FX_BTC_JPY&count=1')
        order_time = res[0]['child_order_date']
        if order_time != befor_order_time:
            print('Ordered')
            post_notification(res)
        befor_order_time = order_time

# build_local_bot()
