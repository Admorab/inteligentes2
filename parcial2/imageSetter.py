# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:27:01 2022

@author: luisd
"""

import cv2
import numpy as np
from Cut import Cut

nameWindow = "Calculadora"

def nothing(x):
    pass

def constructorVentana():
    cv2.namedWindow(nameWindow)
    cv2.createTrackbar("min", nameWindow, 0, 255, nothing)
    cv2.createTrackbar("max", nameWindow, 100, 255, nothing)
    cv2.createTrackbar("kernel", nameWindow, 1, 100, nothing)
    cv2.createTrackbar("areaMin", nameWindow, 500, 10000, nothing)

def calcularAreas(figuras):
    areas = []
    for figuraActual in figuras:
        areas.append(cv2.contourArea(figuraActual))
    return areas


def detectarForma(imagen):    
    global cut, captura, indexImage, categoryImage
    imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gris", imagenGris)
    tamañoKernel = 0
    min = 255
    max = 255
    # # areaMin = 661500
    areaMin = 169900
    # min=cv2.getTrackbarPos("min", nameWindow)
    # max=cv2.getTrackbarPos("max", nameWindow)
    # areaMin = cv2.getTrackbarPos("areaMin", nameWindow)
    # tamañoKernel = cv2.getTrackbarPos("kernel", nameWindow)

    bordes = cv2.Canny(imagenGris, min, max)

    kernel = np.ones((tamañoKernel, tamañoKernel), np.uint8)
    bordes = cv2.dilate(bordes, kernel)
    # cv2.imshow("Bordes", bordes)
    figuras, jerarquia = cv2.findContours(
        bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = calcularAreas(figuras)

    bor = []
    bor.clear()
    i=0
    for fig in figuras:
        if areas and areas[i] > areaMin:
            vertices = cv2.approxPolyDP(
                figuras[i], 0.05*cv2.arcLength(figuras[i], True), True)
            if len(vertices) == 4:
                cv2.drawContours(imagen, [figuras[i]], 0, (0, 0, 255), 2)
                print(i,"area",areas[i])
                bor.append(i)
                
                if captura:
                    img = cut.crop(imagenGris, [figuras[i]])
                    # Izq = Izq[y:y+h, x:x+w]
                    img = cv2.resize(img, (128, 128), cv2.INTER_AREA)
                    cv2.imwrite('Crops/' + str(categoryImage) + "_" + str(indexImage) +
                                '.jpg', img)
                    # cv2.imshow("Recorte", img)
                    indexImage += 1
                    captura = False
                
        i=i+1
    print(bor)
    return imagen

# Apertura cámara
video = cv2.VideoCapture(2)
# constructorVentana()
cut = Cut()
bandera = True
captura = False
categoryImage = 0
indexImage = 0
while bandera:    
    _, imagen = video.read()    
    imagen = detectarForma(imagen)
    imagen = cv2.resize(imagen, (1280, 720), cv2.INTER_AREA)
    cv2.imshow("Imagen", imagen)

    # Parar el programa
    k = cv2.waitKey(5) & 0xFF 
    
    if k == 105:
        categoryImage += 1
        indexImage = 0
    
    if k == 112:
        captura = True

    if k == 27:  # scape
        bandera = False

    # cv2.imshow("Imagen", imagen)
video.release()
cv2.destroyAllWindows()