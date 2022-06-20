import base64
from PIL import Image
import cv2
from io import BytesIO
import numpy as np
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from deteccion import Prediccion

app = Flask(__name__)
cors = CORS(app)
host = "127.0.0.1"
port = 8181
prediccion = Prediccion()
models = []
predicciones = [
    {
        "model_id": "A",
        "results": [
        ]
    },
    {
        "model_id": "B",
        "results": [
        ]
    },
    {
        "model_id": "C",
        "results": [
        ]
    },
]


@app.route("/", methods=['GET'])
def test():
    json = {"message": "Server running OK"}
    return jsonify(json)


@app.route("/predict", methods=['POST'])
def receive():
    global models
    images64 = request.json["images"]
    models = request.json["models"]
    for image in images64:
        imageAux = writeToDisk(image["content"], image["id"])
        predict(imageAux, image["id"])


def predict(image, id):
    global predicciones
    for model in models:
        if model == "A":
            predicciones[0]["results"].append({
                "class": prediccion.predecir(image, "models/model_a.h5"),
                "id-image": id
            })
        elif model == "B":
            predicciones[1]["results"].append({
                "class": prediccion.predecir(image, "models/model_b.h5"),
                "id-image": id
            })
        elif model == "C":
            predicciones[2]["results"].append({
                "class": prediccion.predecir(image, "models/model_c.h5"),
                "id-image": id
            })

    return jsonify({})


def readb64(base64_string):
    return base64.b64decode(base64_string)


def writeToDisk(img_data, id):
    with open("Images/" + str(id) + ".jpg", "wb") as fh:
        image = readb64(img_data)
        fh.write(image)
        return image


@app.after_request
def log_the_status_code(response):
    status_as_integer = response.status_code
    if (status_as_integer == 200):
        response.set_data(json.dumps({
            "state": "success",
            "message": "Predictions made satisfactorily",
            "results": predicciones
        }).encode())
    if (status_as_integer == 400):
        response.set_data(json.dumps({
            "state": "error",
            "message": " Error making predictions",
        }).encode())
    return response


if __name__ == '__main__':
    print("Server running:http://127.0.0.1:8181")
    serve(app, host=host, port=port)
