# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:10:31 2022

@author: luisd
"""
import cv2
# imagen = cv2.imread(r"dataset/train/1/1_1.jpg")
# cv2.imshow("imagen", imagen)

from skimage import io

img = io.imread("dataset/train/1/1_1.jpg")
cv2.imshow("imagen", img)


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
