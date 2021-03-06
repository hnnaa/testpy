# coding:utf-8
import json
import time

from flask import Flask, render_template, abort
from flask import request
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
import sqlite3
app = Flask(__name__)


@app.route("/")
def hello():
    for i in range(20):
        time.sleep(1)
    return "Hello World!"


@app.route("/index", methods=["POST", "GET"])
def index():
    json_str = json.dumps(request.get_json())
    return "<h1>index</h1><p1>" + (json_str or "None") + "</p1>"


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/signin", methods=["GET"])
def signin_form():
    return render_template("form.html")


@app.route("/signin", methods=["POST"])
def signin():
    raise
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin":
        return render_template("signin-ok.html", username=username)
    abort(404)
    return render_template("form.html", message="error user")


if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
