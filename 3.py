import cv2
import numpy as np

image = cv2.imread('image.png')
height, width = image.shape[:2]

cv2.imshow('Original Image', image)

M_large = np.float32([[1, 0, width // 2 + 50], [0, 1, height // 2 + 50]])
shifted_large = cv2.warpAffine(image, M_large, (width, height))

cv2.imshow('Large Shift', shifted_large)

cv2.waitKey(0)
cv2.destroyAllWindows()