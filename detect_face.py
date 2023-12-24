import cv2

img = cv2.imread("my_image.jpeg")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grayimage, 1.1, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 225, 10), 2)


cv2.imshow("Detect Faces", img)
cv2.waitKey(0)