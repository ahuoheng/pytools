# coding=utf-8
import hashlib


def data2md5(data):
    md5str=hashlib.md5(data).hexdigest()
    return md5str

s="123"
print(data2md5(s.encode(encoding='UTF-8')))