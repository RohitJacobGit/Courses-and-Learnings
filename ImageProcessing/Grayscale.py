import cv2
import numpy as np

image = cv2.imread('/Users/rohitanand/Downloads/Simple_image.jpg')
image = cv2.resize(image, (900, 681))

for x in range(300, 600):
    for y in range(0, 680):
        gray = 0.8*image[y, x, 0] + 0.1*image[y, x, 1] + 0.1*image[y, x, 2]
        for c in range(0, 3):
            image[y, x, c] = gray

for x in range(600, 900):
    for y in range(0, 680):
        gray = 0.33*image[y, x, 0] + 0.33*image[y, x, 1] + 0.33*image[y, x, 2]
        for c in range(0, 3):
            image[y, x, c] = gray

cv2.imshow('Simple Image', image)
cv2.waitKey()
