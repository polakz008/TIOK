import cv2
import numpy as np

image = cv2.imread("image.png")

M_numpy = np.ones(image.shape, dtype="uint8") * 50
bright_numpy = image + M_numpy

M_cv2 = np.ones(image.shape, dtype="uint8") * 50
bright_cv2 = cv2.add(image, M_cv2)

cv2.imshow("Original", image)
cv2.imshow("NumPy", bright_numpy)
cv2.imshow("OpenCV", bright_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()