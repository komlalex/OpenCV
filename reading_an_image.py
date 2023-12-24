# Import opencv
import cv2 

### How to read an image
img = cv2.imread("my_image.jpeg")


### Show the image
cv2.imshow("Output Image", img)


cv2.waitKey(0)