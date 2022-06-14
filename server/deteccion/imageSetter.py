# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:33:32 2022

@author: luisd
"""
import os
carpetas = os.listdir('dataset/test')
i = 0
# carpetas = [int(numeric_string) for numeric_string in carpetas]
# carpetas.sort()
print(carpetas)
for carpeta in carpetas: 
    print("Set #:",i)
    j = 0
    images = os.listdir('dataset/test/'+str(carpeta))
    for image in images:
        print("==============================================================")        
        print('dataset/test/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')                        
        os.rename('dataset/test/'+str(carpeta)+'/'+image, 'dataset/test/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')
        # if image.split(".")[1] == "JPEG":            
        #     os.rename('DatasetRAW/'+str(carpeta)+'/'+image, 'DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.JPEG')
        #     print('DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.JPEG')
        # else:
        #     os.rename('DatasetRAW/'+str(carpeta)+'/'+image, 'DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')
        #     print('DatasetRAW/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')                        
        j += 1
    i += 1

