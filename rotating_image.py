import cv2

img = cv2.imread("my_image.jpeg")

height, width = img.shape[:2]

rotateimg = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)

finalimg = cv2.warpAffine(img, rotateimg, (width, height))

cv2.imshow("Rotated Image", finalimg)

cv2.imshow("Original Image", img)

cv2.waitKey()