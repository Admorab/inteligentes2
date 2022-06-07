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
carpetas = os.listdir('Dataset\imagesROW')
i = 1
for carpeta in carpetas: 
    print("i:",i)
    j = 1
    images = os.listdir('Dataset\imagesROW\\'+carpeta)
    for image in images:
        print("==============================================================")
        print(image)
    
        img = cv2.imread('Dataset\imagesROW\\'+carpeta+'\\'+image, cv2.IMREAD_UNCHANGED)
         
        print('Original Dimensions : ',img.shape)
         
        scale_percent = 4.13 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
          
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        resizedAndGray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
         
        print('Resized Dimensions : ',resizedAndGray.shape)
         
        nameImage = str(i)+"\\"+str(i)+"_"+str(j)+".jpg"
        cv2.imwrite("Dataset\\"+nameImage, resizedAndGray)
        
        print("j:",j)
        j += 1
        print("==============================================================")        
    i += 1




