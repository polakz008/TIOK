import cv2
import numpy as np

image = cv2.imread('image.png')


tx = int(input("Podaj przesunięcie w poziomie (tx): "))
ty = int(input("Podaj przesunięcie w pionie (ty): "))

cv2.imshow('Original Image', image)

M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Dynamically Shifted Image', shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()