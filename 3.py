import cv2
import numpy as np

image = cv2.imread("osoba.png")
(B, G, R) = cv2.split(image)

swapped_image = cv2.merge([R, B, G])
cv2.imshow("Swapped", swapped_image)

no_red = cv2.merge([B, G, np.zeros_like(R)])
cv2.imshow("No Red", no_red)

cv2.waitKey(0)
cv2.destroyAllWindows()