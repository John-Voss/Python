import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)
tips_id = [4,8,12,16,20]

def draw_hand_lanMarks(img, hand_lanMarks):
    if hand_lanMarks:
        for land_mark in hand_lanMarks:
            mp_drawing.draw_landmarks(img, land_mark, mp_hands.HAND_CONNECTIONS)

def count_fingers(img, hand_lanMarks, handNo = 0):
    if hand_lanMarks:
        land_marks = hand_lanMarks[handNo].landmark
        fingers = []
        for lm_index in tips_id:
            finger_tip_y = land_marks[lm_index].y
            finger_bottom_y = land_marks[lm_index - 2].y
            
            # Obtenha o valor x da ponta e da parte inferior do polegar
            thumb_tip_x = land_marks[lm_index].x
            thumb_bottom_x = land_marks[lm_index - 2].x

            
            if lm_index != 4:
                if finger_tip_y < finger_bottom_y:
                    fingers.append(1)
                    print('o dedo ', lm_index, ' está aberto!')
                if finger_tip_y > finger_bottom_y:
                    fingers.append(0)
                    print('o dedo', lm_index, 'está fechado!')
            else:
                if thumb_tip_x > thumb_bottom_x:
                    fingers.append(1)
                    print("POLEGAR está Aberto")

                if thumb_tip_x < thumb_bottom_x:
                    fingers.append(0)
                    print("POLEGAR está Fechado")
            
            
        total_fingers = fingers.count(1)
        text = f'Tem {total_fingers} dedos abertos!'
        cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)


while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    results = hands.process(image)
    hand_lanMarks = results.multi_hand_landmarks
    
    draw_hand_lanMarks(image, hand_lanMarks)
    count_fingers(image, hand_lanMarks)
    
    
    
    
    cv2.imshow("Controlador de Midia", image)

    key = cv2.waitKey(25)
    if key == 32:
        break

cv2.destroyAllWindows()