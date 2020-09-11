# coding:utf-8
import time

from flask import Flask
from flask import request
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

app = Flask(__name__)


@app.route("/")
def hello():
    for i in range(20):
        time.sleep(1)
    return "Hello World!"


@app.route("/index", methods=["POST", "GET"])
def index():
    json = request.get_json()
    return "<h1>index</h1>"


if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
    print("abc...")
