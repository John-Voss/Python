import cv2

# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('C:/Users/brand/Downloads/AnthonyShkraba.mp4')

if video.isOpened() == False:
    print("it couldn't be possible to read the video")

height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(video.get(cv2.CAP_PROP_FPS))

# print(height)
# print(width)
# print(fps)

# while True:
#     ret, frame = video.read()
#     cv2.imshow('webcam', frame)
#     if cv2.waitKey(1) == 32:
#         break

# video.release()

video2 = cv2.VideoWriter('C:/Users/brand/Downloads/copia.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while True:
    ret, frame = video.read()
    video2.write(frame)
    cv2.imshow('video', frame)
    if cv2.waitKey(15) == 32:
        break

video2.release()
cv2.destroyAllWindows()