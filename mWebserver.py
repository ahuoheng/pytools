# coding=utf-8
import flask
from flask import Flask, jsonify, request

server = flask.Flask(__name__)

#http://127.0.0.1:8808/get?id=1
@server.route('/get', methods=['get'])
def get():
    params = request.json if request.method == "POST" else request.args
    #print(request.method)  GET
    print(params['id'])

    rs={}
    rs['user']=1
    return jsonify({'result': rs})


@server.route('/post', methods=['post'])
def post():
    params = request.json if request.method == "POST" else request.args

    print(params['rs'])
    return jsonify({'result': request.json})

server.run(host="0.0.0.0", port=8808, debug=True)