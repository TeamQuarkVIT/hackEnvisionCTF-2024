#!/usr/bin/env python3

from flask import Flask, request, Response
from api import strong_method 

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

#let's repalce get, post, etc
#we aim to create a strong method where only quark admins can access flag
@app.route('/flag', methods=strong_method)
def flag():
    return open('flag.txt').read()

@app.after_request
def hide_allowed(response):
    response.headers["Allow"] = ""
    return response

if __name__ == "__main__":
	app.run('0.0.0.0', 1337, debug=False)
