import json
import cv2
import numpy as np
from Cut import Cut
import base64
import os
import requests as http
import timeit


from models.predict_model import Predict

# from predict_model import predict
nameWindow = "Calculadora"


def nothing(x):
    pass


def constructorVentana():
    cv2.namedWindow(nameWindow)
    cv2.createTrackbar("min", nameWindow, 0, 255, nothing)
    cv2.createTrackbar("max", nameWindow, 100, 255, nothing)
    cv2.createTrackbar("kernel", nameWindow, 1, 100, nothing)
    cv2.createTrackbar("areaMin", nameWindow, 500, 1000, nothing)


def calcularAreas(figuras):
    areas = []
    for figuraActual in figuras:
        areas.append(cv2.contourArea(figuraActual))
    return areas


def detectarForma(imagen):
    global captura, indexImage
    cut = Cut()
    imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # imagenHSV=cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
    # cv2.imshow("Gris", imagenGris)
    # cv2.imshow("HSV", imagenHSV)

    # min=cv2.getTrackbarPos("min", nameWindow)
    # max=cv2.getTrackbarPos("max", nameWindow)
    # areaMin = cv2.getTrackbarPos("areaMin", nameWindow)
    # tamañoKernel = cv2.getTrackbarPos("kernel", nameWindow)
    tamañoKernel = 10
    min = 253
    max = 255
    areaMin = 143

    bordes = cv2.Canny(imagenGris, min, max)

    kernel = np.ones((tamañoKernel, tamañoKernel), np.uint8)
    bordes = cv2.dilate(bordes, kernel)
    cv2.imshow("Bordes", bordes)

    # Detección de la figura
    figuras, jerarquia = cv2.findContours(
        bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = calcularAreas(figuras)

    i = 0

    #####
    # last = len(figuras)-1
    last = 0
    if areas and last < len(areas) and areas[last] >= areaMin:
        vertices = cv2.approxPolyDP(
            figuras[last], 0.05 * cv2.arcLength(figuras[last], True), True)
        if len(vertices) == 4:
            cv2.drawContours(imagen, [figuras[last]], 0, (0, 0, 255), 2)

    #####

    if areas and last < len(areas) and captura and areas[last] >= areaMin:

        vertices = cv2.approxPolyDP(
            figuras[last], 0.05 * cv2.arcLength(figuras[last], True), True)
        if len(vertices) == 4:
            mensaje = "Cuadrado"
            cv2.putText(imagen, mensaje, (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.drawContours(imagen, [figuras[last]], 0, (0, 0, 255), 2)

            print(indexImage)
            indexImage = cut.crop(imagenGris, [figuras[last]], indexImage)
        # for figuraActual in figuras:
        #     if areas[i] >= areaMin:
        #         i=i+1
        #         vertices = cv2.approxPolyDP(
        #             figuraActual, 0.05 * cv2.arcLength(figuraActual, True), True)
        #         if len(vertices) == 4:
        #             mensaje = "Cuadrado"
        #             cv2.putText(imagen, mensaje, (10, 70),
        #                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        #             cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)

        #             print(indexImage)
        #             # indexImage = cut.crop(imagenGris, [figuraActual], indexImage)
        captura = False

    return imagen


def readImages():
    images = []
    content = os.listdir('Crops')
    cont = 0
    for c in content:
        images.append(codeImages(cv2.imread("Crops/" + c), cont))
        cont += 1
    return images


def codeImages(image, index):
    retval, buffer = cv2.imencode('.jpg', image)
    image = {
        "id": index,
        "content": base64.b64encode(buffer).decode("utf-8")
    }
    return image


def sendImages64(images, url, id_client):
    # predict = Predict(id_client, images, [id_client])
    predict = {
        "id_client": id_client,
        "images": images,
        "models": [
            1, 2, 3
        ]
    }
    return http.post(url, json=predict).content


# def mostrarMensaje(mensaje, imagen,figuraActual):
#     cv2.putText(imagen, mensaje, (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#     # cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)

# Apertura cámara

video = cv2.VideoCapture(2)
# constructorVentana()
bandera = True
captura = False
images64 = []
indexImage = 0
i = 0
url = "http://127.0.0.1:8181/predict"
while bandera:
    _, imagen = video.read()
    imagen = detectarForma(imagen)
    cv2.imshow("Imagen", imagen)

    # Parar el programa
    k = cv2.waitKey(5) & 0xFF
    if k == 99:  # c
        captura = True
    if k == 101:  # e
        images64 = readImages()
        # sendImages64(images64, url, "1")
        start = timeit.default_timer()
        print("RespuestaServidor:", sendImages64(images64, url, "1"))
        stop = timeit.default_timer()
        print('Time: ', stop - start)

    if k == 27:  # scape
        bandera = False

    cv2.imshow("Imagen", imagen)
video.release()
cv2.destroyAllWindows()
