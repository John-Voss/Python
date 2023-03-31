import cv2
import numpy as np

img = cv2.imread('C:/Users/brand/Downloads/images/image1.jpg')

# DISPLAY THE IMAGE WITH THE ORIGINAL COLOR

# cv2.imshow("Imagem de Exibição",img)
# cv2.waitKey(0)
# print(img)

# DISPLAY THE IMAGE BLACK AND WHITE

# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Escala de cinza",gray_img)
# cv2.waitKey(0)
# print(gray_img)

# CREATING A BLACK AND WHITE IMAGE

# black = np.zeros([600,600])
# black[200:400, 200:400] = 255
# cv2.imshow('Create image black', black)
# cv2.waitKey(0)
# print(black)

# ADDING A TEXT IN A IMAGE

img2 = cv2.imread('C:/Users/brand/Downloads/images/image2.jpg')
rocket = img2[120:360, 400:500]
img2[0:240, 500:600] = rocket
text_to_show = "Let's go!"
cv2.putText(img2, text_to_show, (180,100), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale=2.6, color=(0,0,255))

cv2.imshow('Poster', img2)
cv2.waitKey(0)