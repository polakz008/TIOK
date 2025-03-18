import cv2
import numpy as np

image = cv2.imread('image.png')
cv2.imshow('Original Image', image)

M2 = np.float32([[1, 0, -20], [0, 1, -50]])
shifted2 = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Left and Up', shifted2)

cv2.waitKey(0)
cv2.destroyAllWindows()