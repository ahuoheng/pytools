# coding=utf-8
import json

def str2json(jstr):
    return json.loads(jstr)

jsonstr="{\"message\": \"success感谢\",\"status\": 200}"
js=str2json(jsonstr)
print(js["status"])
