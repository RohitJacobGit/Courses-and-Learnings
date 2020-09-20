import cv2
import numpy as np

image = cv2.imread('/Users/rohitanand/Downloads/Simple_image.jpg')
#image = cv2.resize(image, (800, 681))

# 1024*680
for x in range(0, 523):
    for y in range(0, 680):
        gray = 0.33*image[y, x, 0] + 0.33*image[y, x, 1] + 0.33*image[y, x, 2]
        for c in range(0, 3):
            # image[y, x, 1] = 0
            # image[y, x, c] = min(255, image[y, x, c] + 100)
            # image[y, x, c] = min(255, image[y, x, c]*1.5)
            image[y, x, c] = gray

cv2.imshow('Simple Image', image)
cv2.waitKey()
