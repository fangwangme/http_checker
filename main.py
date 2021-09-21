#! /usr/bin/python3
# coding:utf-8

"""
@author:Fang Wang
@date:2021-09-21
@desc:
"""
import json

from flask import Flask, request, jsonify
from logger import logger

app = Flask(__name__)


@app.route("/ip")
def check_ip():
    request_ip = request.remote_addr
    logger.info("Got a request from {} with headers {}".format(request_ip, json.dumps(dict(request.headers))))
    return jsonify({"ip": request_ip})


@app.route("/")
def hello_world():
    request_ip = request.remote_addr
    logger.info("Got a request from {} with headers {}".format(request_ip, json.dumps(dict(request.headers))))
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
