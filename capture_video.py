import cv2

video = cv2.VideoCapture(0)



while True:
    check, frame = video.read()
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)