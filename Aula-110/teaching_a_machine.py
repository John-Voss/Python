import cv2
import numpy as np

import tensorflow as tf

mymodel = tf.keras.models.load_model("C:/Users/brand/Downloads/keras_model.h5")

video = cv2.VideoCapture(0)

while True:

    check,frame = video.read()

    # Altere o dado de entrada:

    # 1. Redimensione a imagem

    img = cv2.resize(frame,(224,224))

    # 2. Converta a imagem em um array Numpy e aumente a dimensão

    test_image = np.array(img, dtype=np.float32)
    test_image = np.expand_dims(test_image, axis=0)

    # 3. Normalize a imagem
    normalized_image = test_image / 255.0

    # Preveja o resultado
    prediction = mymodel.predict(normalized_image)

    oculos = int(prediction[0][0] * 100)
    sem_oculos = int(prediction[0][1] * 100)

    print(f"Previsão: Com Óculos => {oculos}% ---- Sem Óculos => {sem_oculos}%")
    
    cv2.imshow("Resultado",frame)
            
    key = cv2.waitKey(1)

    if key == 32:
        print("Fechando")
        break

video.release()