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

app = Flask(__name__)
cors = CORS(app)
host = "127.0.0.1"
port = 8181


@app.route("/", methods=['GET'])
def test():
    json = {"message": "Server running OK"}
    return jsonify(json)


@app.route("/predict", methods=['POST'])
def receive():    
    # json ={"llave":"valor"}     
    # print(request.json)
    # print(request)
    images64 = request.json["images"]    
    for image in images64:
        writeToDisk(image["content"], image["id"])
    return jsonify({})

def readb64(base64_string):
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

def writeToDisk(img_data, id):        
    with open("Images/"+str(id)+".jpg", "wb") as fh:
        fh.write(base64.decodebytes(readb64(img_data)))

@app.after_request
def log_the_status_code(response):
    status_as_integer = response.status_code
    if(status_as_integer == 200):
        response.set_data(json.dumps({
            "state": "success",
            "message": "Predictions made satisfactorily",
            "results": [
                {
                    "model_id": 1,
                    "results": [
                        {
                            "class": 0,
                            "id-image": 88
                        },
                        {
                            "class": 1,
                            "id-image": 99
                        }
                    ]
                },
                {
                    "model_id": 2,
                    "results": [
                        {
                            "class": 1,
                            "id-image": 88
                        },
                        {
                            "class": 0,
                            "id-image": 99
                        }
                    ]
                }

            ]
        }).encode())
    if (status_as_integer == 400):
        response.set_data(json.dumps({
            "state": "error",
            "message": " Error making predictions",
        }).encode())
    print(response.data)
    return response





if __name__ == '__main__':
    print("Server running:http://127.0.0.1:8181")
    serve(app, host=host, port=port)
