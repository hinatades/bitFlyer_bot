
# -*- coding: utf-8 -*-

import csv
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
    """
    """
    method = 'GET'
    api_endpoint = 'https://api.bitflyer.jp'
    timestamp = str(time.time())
    text = timestamp + method + path  # + body
    sign = hmac.new(SECRET_KEY.encode(), text.encode(), hashlib.sha256).hexdigest()
    res = requests.get(
        api_endpoint + path,
        headers={
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
    text = _process_array_for_slack(_process_json_array(USER_NAME, info))
    requests.post(
        api_endpoint,
        data=json.dumps({
            "username": "btcfxjp",
            "text": text,
            "icon_emoji": ":ghost:",
        })
    )


def _process_json_array(user, json_dict):

    new_list = []
    for i in json_dict:
        new_dict = {'ユーザー': user}
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


def _process_array_for_slack(json_array):

    text = ''
    for json_dict in json_array:
        for k, v in json_dict.items():
            text += str(k) + ': ' + str(v) + '\n'
        text += '\n'
    return text


def build_order_bot():
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
            post_notification(res)
            print('Ordered: ' + _process_json_array(USER_NAME, res)[0]['注文時刻'])
        befor_order_time = order_time


def build_ticker_bot(count=None):
    """
    """
    num = 0
    res = []
    if not count:
        count = 1
    while (num < 5):
        sleep(1)
        res = get_info('/v1/getticker?product_code=FX_BTC_JPY&count=' + count)
        post_ticker_notification(res)


def make_ticker_csv(count=1):
    """
    """

    with open("ticker.csv", "w", newline="") as f:

        keys = [
            'timestamp', 'product_code', 'tick_id',
            'best_ask', 'best_ask_size', 'best_bid', 'best_bid_size',
            'total_ask_depth', 'total_bid_depth', 'ltp',
            'volume', 'volume_by_product'
        ]
        writer = csv.DictWriter(f, fieldnames=keys, delimiter=",", quotechar='"')
        writer.writeheader()
        before_timestamp = ''
        for i in range(count):
            res = get_info('/v1/getticker?product_code=FX_BTC_JPY')
            try:
                dt = datetime.strptime(res['timestamp'], '%Y-%m-%dT%H:%M:%S.%f')
                res['timestamp'] = dt.astimezone(timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
            except ValueError:
                dt = datetime.strptime(res['timestamp'], '%Y-%m-%dT%H:%M:%S')
                res['timestamp'] = dt.astimezone(timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
            sleep(0.3)
            if res['timestamp'] != before_timestamp:
                writer.writerow(res)
                print(res.values())
                before_timestamp = res['timestamp']


def post_ticker_notification(info):
    """
    Post notification to #dev
    """
    api_endpoint = SLACK_URL
    text = _process_dict_for_slack(_process_ticker_json_dict(info))
    requests.post(
        api_endpoint,
        data=json.dumps({
            "username": "btcfxjp",
            "text": text,
            "icon_emoji": ":ghost:",
        })
    )


def _process_ticker_json_dict(json_dict):
    """
    """
    new_dict = {}
    print(json_dict)
    for k, v in json_dict.items():
        if k == 'timestamp':
            try:
                dt = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                jst_time = dt.astimezone(timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
            except ValueError:
                dt = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
                jst_time = dt.astimezone(timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')
            new_dict['time'] = jst_time
        elif k == 'ltp':
            new_dict['price'] = v
    return new_dict


def _process_dict_for_slack(json_dict):
    """
    """

    text = json.dumps(json_dict)
    return text


make_ticker_csv(100)
