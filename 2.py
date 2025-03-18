import cv2
import numpy as np

black_image = np.zeros((400, 400, 3), dtype=np.uint8)

cv2.rectangle(black_image, (0, 0), (100, 50), (0, 255, 0), -1)

cv2.rectangle(black_image, (300, 350), (399, 399), (0, 0, 255), 3)

cv2.imwrite('images/rectangles.jpg', black_image)

cv2.imshow('Rectangles', black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()