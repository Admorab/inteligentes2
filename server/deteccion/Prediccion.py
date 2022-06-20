from tensorflow.python.keras.models import load_model
import numpy as np
import cv2


class Prediccion():
    def __init__(self):
        pass

    def predecir(self, imagen, ruta):
        modelo = load_model(ruta)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagen = cv2.resize(imagen, (256, 256))
        imagen = imagen.flatten()
        imagen = imagen / 255
        imagenesCargadas = []
        imagenesCargadas.append(imagen)
        imagenesCargadasNPA = np.array(imagenesCargadas)
        predicciones = modelo.predict(x=imagenesCargadasNPA)
        print("Predicciones=", predicciones)
        clasesMayores = np.argmax(predicciones, axis=1)
        return clasesMayores[0]
