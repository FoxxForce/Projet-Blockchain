#!/usr/bin/env python3
from node import *
from flask import Flask, jsonify

app = Flask(__name__)
node = Node("225.1.2.5")
node.request_blockchain()

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    node.request_blockchain()
    return jsonify(node.blockchain.blockchain_to_string())

if __name__ == "__main__":
    app.run()

