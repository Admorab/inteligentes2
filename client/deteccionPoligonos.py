# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:59:13 2022

@author: luisd
"""

import cv2
import numpy as np

nameWindow="Calculadora"
def nothing(x):
    pass
def constructorVentana():
    cv2.namedWindow(nameWindow)
    cv2.createTrackbar("min",nameWindow,0,255,nothing)
    cv2.createTrackbar("max", nameWindow, 100, 255, nothing)
    cv2.createTrackbar("kernel", nameWindow, 1, 100, nothing)
    cv2.createTrackbar("areaMin", nameWindow, 500, 10000, nothing)
    
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
    
    min=cv2.getTrackbarPos("min", nameWindow)
    max=cv2.getTrackbarPos("max", nameWindow)
    bordes=cv2.Canny(imagenGris,min,max)
    
    tamañoKernel=cv2.getTrackbarPos("kernel", nameWindow)
    kernel=np.ones((tamañoKernel,tamañoKernel),np.uint8)
    bordes=cv2.dilate(bordes,kernel)
    cv2.imshow("Bordes",bordes)
    
    #Detección de la figura
    figuras,jerarquia=cv2.findContours(bordes,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas=calcularAreas(figuras)
    areaMin=cv2.getTrackbarPos("areaMin", nameWindow)
    i=0
    for figuraActual in figuras:
        if areas[i]>=areaMin:
            i=i+1
            vertices=cv2.approxPolyDP(figuraActual,0.05*cv2.arcLength(figuraActual,True),True)
            if len(vertices) == 3:
                mensaje="Triangulo"
                cv2.putText(imagen, mensaje, (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)
            if len(vertices) == 4:
                mensaje="Cuadrado"
                cv2.putText(imagen, mensaje, (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)
            if len(vertices) == 5:
                mensaje="Pentagono"
                cv2.putText(imagen, mensaje, (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)
    return imagen

def mostrarMensaje(mensaje, imagen,figuraActual):
    cv2.putText(imagen, mensaje, (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.drawContours(imagen, [figuraActual], 0, (0, 0, 255), 2)
    
#Apertura cámara
video=cv2.VideoCapture(0)
constructorVentana()
bandera=True
while bandera:
    _,imagen = video.read()
    imagen=detectarForma(imagen)
    cv2.imshow("Imagen", imagen)
    #Parar el programa
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        bandera=False
video.release()
cv2.destroyAllWindows()