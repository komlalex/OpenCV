import  cv2

img = cv2.imread("my_image.jpeg")

height, width = img.shape[:2]

start_row, start_column = int(height * 0.15), int(width * 0.15)

end_row, end_column = int(height * 0.65), int(width * 0.65)

cropped = img[start_row:end_row, start_column:end_column]

cv2.imshow("Cropped", cropped)
cv2.imshow("Original", img)

cv2.waitKey(0)