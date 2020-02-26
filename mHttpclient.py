# coding=utf-8
import json
import requests


def get(url):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    rs = response.text.encode('utf8')
    return rs

url = "http://myip.ipip.net/"
rs=get(url)
print(rs)
