from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
host = "127.0.0.1"
port = 8181


@app.route("/", methods=['GET'])
def test():
    json = {"message": "Server running OK"}
    return jsonify(json)


@app.route("/data", methods=['POST'])
def receive(data):
    print(data)
    json = {"message": "Server running OK"}
    return jsonify(json)


if __name__ == '__main__':
    print("Server running:http://127.0.0.1:8181")
    serve(app, host=host, port=port)
