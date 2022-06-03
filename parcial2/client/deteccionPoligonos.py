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

    tamañoKernel = 10
    min = 253
    max = 255
    areaMin = 143

    bordes = cv2.Canny(imagenGris, min, max)

    kernel = np.ones((tamañoKernel, tamañoKernel), np.uint8)
    bordes = cv2.dilate(bordes, kernel)
    figuras, jerarquia = cv2.findContours(
        bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = calcularAreas(figuras)

    
   
    posIzq = 6
    posDer = 1
    for ver in [posDer, posIzq]:        
        if areas[ver]> areaMin:        
            vertices=cv2.approxPolyDP(figuras[ver],0.05*cv2.arcLength(figuras[ver],True),True)
            if len(vertices) == 4:                
                cv2.drawContours(imagen, [figuras[ver]], 0, (0, 0, 255), 2)
                
    Izq = cut.crop(imagenGris, [figuras[posIzq]], indexImage)
    cv2.imshow("Izq", Izq)
    cv2.moveWindow("Izq", 40,30) 
    
    Der = cut.crop(imagenGris, [figuras[posDer]], indexImage)
    cv2.imshow("Der", Der)
    cv2.moveWindow("Der", 1000,30) 
    

    return imagen



# Apertura cámara

video = cv2.VideoCapture(1)
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

    if k == 27: #scape
        bandera = False

    cv2.imshow("Imagen", imagen)
video.release()
cv2.destroyAllWindows()
