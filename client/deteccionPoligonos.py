# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:59:13 2022

@author: luisd
"""

import cv2
import numpy as np
from Cut import Cut
import base64
import os


nameWindow="Calculadora"
def nothing(x):
    pass
def constructorVentana():
    cv2.namedWindow(nameWindow)
    cv2.createTrackbar("min",nameWindow,0,255,nothing)
    cv2.createTrackbar("max", nameWindow, 100, 255, nothing)
    cv2.createTrackbar("kernel", nameWindow, 1, 100, nothing)
    cv2.createTrackbar("areaMin", nameWindow, 500, 1000, nothing)
    
def calcularAreas(figuras):
    areas=[]
    for figuraActual in figuras:
        areas.append(cv2.contourArea(figuraActual))
    return areas    
def detectarForma(imagen):
    imagenGris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    # imagenHSV=cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
    # cv2.imshow("Gris", imagenGris)
    # cv2.imshow("HSV", imagenHSV)
    
    # min=cv2.getTrackbarPos("min", nameWindow)
    # max=cv2.getTrackbarPos("max", nameWindow)
    min=196
    max=255
    
    bordes=cv2.Canny(imagenGris,min,max)
    
    tamañoKernel=cv2.getTrackbarPos("kernel", nameWindow)
    tamañoKernel=10
    kernel=np.ones((tamañoKernel,tamañoKernel),np.uint8)
    bordes=cv2.dilate(bordes,kernel)
    cv2.imshow("Bordes",bordes)
    
    #Detección de la figura
    figuras,jerarquia=cv2.findContours(bordes,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas=calcularAreas(figuras)
    areaMin=cv2.getTrackbarPos("areaMin", nameWindow)
    areaMin=0
    i=0
    cut = Cut()    
    for figuraActual in figuras:
        if areas[i]>=areaMin:
            i=i+1
            vertices=cv2.approxPolyDP(figuraActual,0.05*cv2.arcLength(figuraActual,True),True)            
            if len(vertices) == 4:
                mensaje="Cuadrado"
                cv2.putText(imagen, mensaje, (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)
                cut.crop(imagenGris, [figuraActual], 1)
                

    return imagen





def readImages():
    images = []
    content = os.listdir('Crops')
    for c in content:        
        images.append(codeImages(cv2.imread("Crops/"+c)))
    return images
    

def codeImages(image):
    retval, buffer = cv2.imencode('.jpg', image)
    return base64.b64encode(buffer)
    

# def mostrarMensaje(mensaje, imagen,figuraActual):
#     cv2.putText(imagen, mensaje, (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#     # cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)
    
#Apertura cámara
# cut = Cut()
video=cv2.VideoCapture(0)
constructorVentana()
bandera=True
mostrar=False
images64 = []
while bandera:
    _,imagen = video.read()     
    
    #Parar el programa
    k = cv2.waitKey(5) & 0xFF
    if k == 101:
        images64 = readImages()
        print(images64)
    if k == 99:
        mostrar = True     
    if k == 27:
        bandera=False
    if mostrar:
        imagen=detectarForma(imagen)  
        cv2.imshow("Imagen", imagen)
        # cut.crop()
    cv2.imshow("Imagen", imagen)
video.release()
cv2.destroyAllWindows()