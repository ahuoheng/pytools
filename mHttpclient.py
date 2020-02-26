#  -*-  coding:utf-8  -*-
import json
import requests

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

def postmultipart(url,formdata):
    register_openers()
    datagen, headers = multipart_encode(formdata )
    request = urllib2.Request(url, datagen, headers)
    return urllib2.urlopen(request).read()


def get(url):
    payload = {}
    headers = {'Cookie': 'SESSION=N'}
    response = requests.request("GET", url, headers=headers, data=payload)
    rs = response.text
    return rs

def postjson(url,postdata):
    payload = postdata
    headers = {
      'Content-Type': 'application/json',
      'userName': 'admin'
    }
    response = requests.request("POST", url, headers=headers, data = payload)

    return  response.text

url = "http://myip.ipip.net/"
rs=get(url)
print(rs)

postdata="{\"user_id\":\"00000002\", \"phone\":\"00000002\", \"status\":\"UNUSED\"}"
postjson(url,postdata)

#formdata=[ ('Img1', open('testdata/face.jpg', 'rb')) ,('Img2', open('2.jpg', 'rb')) ]
#postmultipart(url,formdata)