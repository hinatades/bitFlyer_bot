
# -*- coding: utf-8 -*-

import json
import requests
import time
import hmac
import hashlib
from pytz import timezone
from datetime import datetime
from key import API_KEY, SECRET_KEY, SLACK_URL


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
        data=json.dumps({"text": str(_process_json_array(info))})
    )


def _process_json_array(json_array):

    new_list = []
    for i in json_array:
        new_dict = {'user': ' @gokigoki '}
        for k, v in i.items():
            if k == 'size':
                new_dict['枚数'] = v
            elif k == 'child_order_date':
                dt = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
                jst_time = dt.astimezone(timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
                new_dict['注文時刻'] = jst_time
            elif k == 'side':
                new_dict['注文'] = v
        new_list.append(new_dict)
    return new_list
