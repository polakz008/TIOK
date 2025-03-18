import cv2
import numpy as np

black_image = np.zeros((300, 300, 3), dtype=np.uint8)

cv2.circle(black_image, (40, 40), 40, (255, 0, 0), -1)

cv2.circle(black_image, (150, 150), 60, (0, 0, 255), -1)

cv2.imwrite('images/circles.jpg', black_image)

cv2.imshow('Circles', black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()