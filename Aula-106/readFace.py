import cv2

haarsCascade = cv2.CascadeClassifier("C:/Users/brand/Downloads/haarcascade_frontalface_default.xml")
image = cv2.imread("C:/Users/brand/Downloads/4f.jpg")
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = haarsCascade.detectMultiScale(imageGray)

for(x, y, w, h)in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
cv2.imshow('image', image)
cv2.waitKey(0)