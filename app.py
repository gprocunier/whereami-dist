from flask import Flask, jsonify, request, Response, send_from_directory, redirect
import json
import requests
from ipwhois import IPWhois


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/index.html")


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('dist', path)


@app.route("/api/whereami")
def whereami():
    ip = requests.get('https://api.ipify.org').text
    w = IPWhois(ip)

    return jsonify({"public_ip": ip, "whereami": w.lookup_whois()})


app.run(host="0.0.0.0", port=8080)
