import cv2
import numpy as np

black_image = np.zeros((300, 300, 3), dtype=np.uint8)

center = (150, 150)

top_left = (center[0] - 50, center[1] - 50)
bottom_right = (center[0] + 50, center[1] + 50)
cv2.rectangle(black_image, top_left, bottom_right, (0, 0, 255), -1)

cv2.circle(black_image, center, 30, (255, 0, 0), -1)

cv2.imwrite('images/complex_shape.jpg', black_image)

cv2.imshow('Complex Shape', black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()