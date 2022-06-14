# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:10:31 2022

@author: luisd
"""
# import cv2
# imagen = cv2.imread(r"dataset/train/1/1_1.jpg")
# # print(imagen)
# cv2.imshow("imagen", imagen)
# cv2.waitKey(0)
# 
# from skimage import io

# img = io.imread(r"dataset/train/1/test.jpg")
# cv2.imshow("imagen", img)


# import os
# carpetas = os.listdir('dataset/train')
# i = 1
# # carpetas = [int(numeric_string) for numeric_string in carpetas]
# # carpetas.sort()
# print(carpetas)
# for carpeta in carpetas:
#     print("Set #:",i)
#     j = 1
#     images = os.listdir('dataset/train/'+str(carpeta))
#     for image in images:
#         print("==============================================================")
#         print(image)
#         os.rename('dataset/train/'+str(carpeta)+'/'+image, 'dataset/train/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')
#         print('dataset/train/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')
#         j += 1
#     i += 1





import base64

import tensorflow as tf
import keras
import numpy as np
import cv2
# from Prediccion import Prediccion


#Se usan las siguientes librerias para trabajo con red Neuronal

from keras.models import Sequential
from keras.layers import InputLayer,Input,Conv2D, MaxPool2D,Reshape,Dense,Flatten

from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd


def cargarDatos(fase, numeroCategorias, limite, width, height):
    imagenesCargadas=[]
    valorEsperado=[]
    text = ""
    try:
        for categoria in range(0, numeroCategorias):
            for idImagen in range(0, limite[categoria]):
                ruta=fase+str(categoria)+"/"+str(categoria)+"_"+str(idImagen)+".jpg"
                text=text+ruta+"\n"
                
        #         imagen=cv2.imread(ruta)
        #         imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        #         imagen = cv2.resize(imagen, (width, height))
        #         imagen=imagen.flatten()
        #         imagen=imagen/255
        #         imagenesCargadas.append(imagen)
        #         probabilidades=np.zeros(numeroCategorias)
        #         probabilidades[categoria]=1
        #         valorEsperado.append(probabilidades)
        # imagenes_entrenamiento = np.array(imagenesCargadas)
        # valores_esperados = np.array(valorEsperado)
    
        # print("CANTIDAD DE IMAGINES", len(imagenes_entrenamiento))
        # print("CANTIDAD DE VALORES", len(valores_esperados))
    
        # return imagenes_entrenamiento, valores_esperados
    except:
        pass
    with open('files.txt', 'w') as f:
        f.write(text)

width = 256
height = 256
pixeles = width * height

# Si es a blanco y negro es -> 1 si es RGB es -> 3
num_channels = 3
img_shape = (width, height, num_channels)

# Cant elementos a clasifica
num_clases = 5
cantidad_datos_entenamiento=[1797,367,305,1939,1613]
cantidad_datos_pruebas=[30,30,30,30,30]

##Carga de los datos
# imagenes, probabilidades = 
cargarDatos("dataset/train/", num_clases, cantidad_datos_entenamiento, width, height)
# print(imagenes)