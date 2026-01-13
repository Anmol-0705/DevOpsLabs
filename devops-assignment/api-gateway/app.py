from flask import Flask
import requests

app = Flask(__name__)

@app.route("/a")
def route_a():
    return requests.get("http://service-a:5001/service-a").text

@app.route("/b")
def route_b():
    return requests.get("http://service-b:5002/service-b").text

app.run(host="0.0.0.0", port=8080)
