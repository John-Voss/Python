import cv2

haarsCascade = cv2.CascadeClassifier("C:/Users/brand/Downloads/haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    rat, frame = video.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haarsCascade.detectMultiScale(frameGray, 1.1, 5)
    
    for(x, y, w, h)in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    
    cv2.imshow('video', frame)
    if cv2.waitKey(25) == 32:
        break
    
video.release()
cv2.destroyWindows()
    

