"""
How to get information such as width, height etc. from an image
"""

import cv2

img = cv2.imread("my_image.jpeg")

print(img.shape)

print(f"Height: {img.shape[0]}, Width: {img.shape[1]}, Depth: {img.shape[2]}")

cv2.waitKey(0)