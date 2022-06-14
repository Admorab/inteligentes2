# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:33:32 2022

@author: luisd
"""
import os
carpetas = os.listdir('DatasetRAW')
i = 1
# carpetas = [int(numeric_string) for numeric_string in carpetas]
# carpetas.sort()
print(carpetas)
for carpeta in carpetas: 
    print("Set #:",i)
    j = 1
    images = os.listdir('DatasetRAW/'+str(carpeta))
    for image in images:
        print("==============================================================")
        if image.split(".")[1] == "JPEG":            
            os.rename('DatasetRAW/'+str(carpeta)+'/'+image, 'DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.JPEG')
            print('DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.JPEG')
        else:
            os.rename('DatasetRAW/'+str(carpeta)+'/'+image, 'DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')
            print('DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')                        
        j += 1
    i += 1

