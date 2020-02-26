# coding=utf-8
import base64

def data2b64(data):
    b64str = base64.b64encode(data)
    return b64str

def b642data(b64strs):
    data = base64.b64decode(b64strs)
    return data

data="abc123"
b64=data2b64(data.encode('utf-8'))
print(str(b64,'utf-8'))
print(b642data(b64))