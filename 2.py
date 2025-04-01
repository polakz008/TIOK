import cv2
import numpy as np

image = cv2.imread("image.png")

M_numpy = np.ones(image.shape, dtype="uint8") * 150
overexposed_numpy = image + M_numpy

cv2.imshow("Original", image)
cv2.imshow("NumPy", overexposed_numpy)
cv2.waitKey(0)
cv2.destroyAllWindows()