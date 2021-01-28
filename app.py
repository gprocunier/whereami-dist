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
    w = IPWhois(ip).lookup_whois()

    print("public_ip: " + ip)
    print("provider:" + w['nets'][0]['description'])
    print("asn: " + w['asn'])

    return jsonify({
        "public_ip": ip,
        "provider": w['nets'][0]['description'],
        "asn": w['asn']
    })


app.run(host="0.0.0.0", port=8080)
