
from flask import Flask, request
import os
import socket

# Connect to Redis
# redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Hello, world!", 200
    elif request.method == "POST": 
        return "This method is unsupported.", 405

@app.route("/check", methods=["GET","POST"])
def check():
    if request.method == "GET":
        return f"GET message received", 200
    elif request.method == "POST": 
        msg = request.args.get('msg','')
        if msg:
            return f"POST message received: {msg}", 200
        else:
            return "This method is unsupported.", 405

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
