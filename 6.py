import cv2
import numpy as np

image = cv2.imread('opencw.png')

B, G, R = cv2.split(image)

swapped = cv2.merge((R, G, B))

no_green = cv2.merge((B, np.zeros_like(G), R))

cv2.imshow('Original', image)
cv2.imshow('Red and Blue Swapped', swapped)
cv2.imshow('No Green Channel', no_green)
cv2.waitKey(0)
cv2.destroyAllWindows()
