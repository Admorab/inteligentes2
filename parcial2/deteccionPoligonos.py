import cv2
import numpy as np
from Cut import Cut
from Prediccion import Prediccion

nameWindow = "Calculadora"
prediccion = Prediccion('models/models/modeloA.h5')


def nothing(x):
    pass


def constructorVentana():
    cv2.namedWindow(nameWindow)
    cv2.createTrackbar("min", nameWindow, 0, 255, nothing)
    cv2.createTrackbar("max", nameWindow, 100, 255, nothing)
    cv2.createTrackbar("kernel", nameWindow, 1, 100, nothing)
    cv2.createTrackbar("areaMin", nameWindow, 500, 100000, nothing)


def calcularAreas(figuras):
    areas = []
    for figuraActual in figuras:
        areas.append(cv2.contourArea(figuraActual))
    return areas


def detectarForma(imagen):
    global captura, indexImage, predict
    cut = Cut()
    imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gris", imagenGris)
    tamañoKernel = 10
    min = 255
    max = 255
    areaMin = 70068
    # min=cv2.getTrackbarPos("min", nameWindow)
    # max=cv2.getTrackbarPos("max", nameWindow)
    # areaMin = cv2.getTrackbarPos("areaMin", nameWindow)
    # tamañoKernel = cv2.getTrackbarPos("kernel", nameWindow)

    bordes = cv2.Canny(imagenGris, min, max)

    kernel = np.ones((tamañoKernel, tamañoKernel), np.uint8)
    bordes = cv2.dilate(bordes, kernel)
    cv2.imshow("Bordes", bordes)
    figuras, jerarquia = cv2.findContours(
        bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = calcularAreas(figuras)

    posIzq = 23
    posDer = 3
    # try: 
    #     for ver in [ posIzq, posDer]:
    #         if areas and areas[ver] > areaMin:
    #             vertices = cv2.approxPolyDP(
    #                 figuras[ver], 0.05*cv2.arcLength(figuras[ver], True), True)
    #             if len(vertices) == 4:
    #                 cv2.drawContours(imagen, [figuras[ver]], 0, (0, 0, 255), 2)
    # except:
    #     pass
    i=0
    for fig in figuras:
        if areas and areas[i] > areaMin:
            vertices = cv2.approxPolyDP(
                figuras[i], 0.05*cv2.arcLength(figuras[i], True), True)
            if len(vertices) == 4:
                cv2.drawContours(imagen, [figuras[i]], 0, (0, 0, 255), 2)
                print(i,"area",areas[i])
        i=i+1


    # print(type(figuras.item(posIzq)))
    # if np.logical_and(figuras[posIzq] != None, figuras[posDer] != None):
    # if list(figuras)[posIzq]:
    try:
        
        y=30
        x=30
        h=250
        w=200
        
        
        Izq = cut.crop(imagenGris, [figuras[posIzq]], indexImage)
        Izq = Izq[y:y+h, x:x+w]
        Izq = cv2.resize(Izq, (128, 128), cv2.INTER_AREA)
        cv2.imshow("Izq", Izq)
        cv2.moveWindow("Izq", 40,30)
        
        Izq = cv2.Canny(Izq, 255, 255)
        kernel = np.ones((1, 1), np.uint8)
        Izq = cv2.dilate(Izq, kernel)
        cv2.imshow("IzqPredict", Izq)
        cv2.moveWindow("IzqPredict", 40,200)
        
    
        Der = cut.crop(imagenGris, [figuras[posDer]], indexImage)
        Der = Der[y:y+h, x:x+w]
        Der = cv2.resize(Der, (128, 128), cv2.INTER_AREA)
        cv2.imshow("Der", Der)
        cv2.moveWindow("Der", 180,30)
        
        Der = cv2.Canny(Der, 255, 255)
        kernel = np.ones((1, 1), np.uint8)
        Der = cv2.dilate(Der, kernel)
        cv2.imshow("DerPredict", Der)
        cv2.moveWindow("DerPredict", 180,200)
        
        
        if predict:            
            izqVal = prediccion.predecir(Izq)+1
            derVal = prediccion.predecir(Der)+1
            total = izqVal+derVal
            print("La suma de las cartas",izqVal,derVal,"es:",total)
            predict = False
    except:
        pass
    return imagen


# Apertura cámara
# constructorVentana()
video = cv2.VideoCapture(2)
bandera = True
predict = False
images64 = []
indexImage = 0
i = 0
url = "http://127.0.0.1:8181/predict"
acumulado = 0
while bandera:
    _, imagen = video.read()    
    imagen = detectarForma(imagen)
    imagen = cv2.resize(imagen, (1280, 720), cv2.INTER_AREA)
    cv2.imshow("Imagen", imagen)

    # Parar el programa
    k = cv2.waitKey(5) & 0xFF
    if k == 112:
        predict = True

    if k == 27:  # scape
        bandera = False

    # cv2.imshow("Imagen", imagen)
video.release()
cv2.destroyAllWindows()
