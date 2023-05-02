import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("C:/Users/brand/Downloads/converted_keras/keras_model.h5")

video = cv2.VideoCapture(0)

while True :
    check, frame = video.read()
    
    img = cv2.resize(frame, (224,224))
    
    test_image = np.array(img, dtype=np.float32)
    test_image = np.expand_dims(test_image, axis=0)
    
    normalized_image = test_image/255.0
    
    prediction = model.predict(normalized_image)
    
    pedra = int(prediction[0][0] * 100)
    papel = int(prediction[0][1] * 100)
    tesoura = int(prediction[0][2] * 100)
    
    resultado = f'PEDRA: {pedra}% ----- PAPEL: {papel}% ----- TESOURA: {tesoura}%'
    cv2.putText(frame, resultado, (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    
    cv2.imshow('jogo', frame)
    
    key = cv2.waitKey(1)
    
    if key == 32:
        print('fechando')
        break
    
video.release()