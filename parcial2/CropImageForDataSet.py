# # -*- coding: utf-8 -*-
# """
# Created on Tue Jun  7 18:02:08 2022

# @author: luisd
# """

# # Import packages
# import cv2

# img = cv2.imread('test.jpg')
# print(img.shape) # Print image shape
# cv2.imshow("original", img)

# # Cropping an image
# cropped_image = img[80:280, 150:330]

# # Display cropped image
# cv2.imshow("cropped", cropped_image)

# # Save the cropped image
# cv2.imwrite("Cropped Image.jpg", cropped_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()





# import cv2
 
# img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
 
# print('Original Dimensions : ',img.shape)
 
# scale_percent = 4.13 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
  
# # resize image
# resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# resizedAndGray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
 
# print('Resized Dimensions : ',resizedAndGray.shape)
 
# cv2.imwrite("ResizedAndGray.jpg", resizedAndGray)


# cv2.imshow("Resized image", resizedAndGray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#####
import cv2
import os
import numpy as np
# carpetas = os.listdir('models\dataset\imagesROW')
# i = 1
# carpetas = [int(numeric_string) for numeric_string in carpetas]
# carpetas.sort()
# print(carpetas)
# for carpeta in carpetas: 
#     print("Set #:",i)
#     j = 1
#     images = os.listdir('models\dataset\imagesROW\\'+str(carpeta))
#     for image in images:
#         print("==============================================================")
#         print(image)
#         print('models\dataset\test\\'+str(carpeta)+'\\'+str(i)+'_'+str(j)+'.jpg')
#         img = cv2.imread('models\dataset\imagesROW\\'+str(carpeta)+'\\'+image, cv2.IMREAD_UNCHANGED)
         
#         print('Original Dimensions : ',img.shape)
         
#         scale_percent = 4.13 # percent of original size
#         width = int(img.shape[1] * scale_percent / 100)
#         height = int(img.shape[0] * scale_percent / 100)
#         dim = (width, height)
          
#         # resize image
#         resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
#         resizedAndGray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
         
#         print('Resized Dimensions : ',resizedAndGray.shape)
        
        
#         bordes = cv2.Canny(resizedAndGray, 255, 255)

#         kernel = np.ones((1, 1), np.uint8)
#         bordes = cv2.dilate(bordes, kernel)
         
#         nameImage = str(i)+"\\"+str(i)+"_"+str(j)+".jpg"
#         cv2.imwrite("models\dataset\\"+nameImage, bordes)
        
#         print("Image #:",j)
#         j += 1
#         print("==============================================================")        
#     i += 1
    
carpetas = os.listdir('models/dataset/test')
i = 0
carpetas = [int(numeric_string) for numeric_string in carpetas]
carpetas.sort()
print(carpetas)
for carpeta in carpetas: 
    print("Set #:",i)
    j = 0
    images = os.listdir('models/dataset/test/'+str(carpeta))
    for image in images:
        print("==============================================================")
        print(image)
        os.rename('models/dataset/test/'+str(carpeta)+'/'+image, 'models/dataset/test/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')
        print('models/dataset/test/'+str(carpeta)+'/'+str(i)+'_'+str(j)+'.jpg')
        j += 1
    i += 1




