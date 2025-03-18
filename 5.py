import cv2
import numpy as np

black_image = np.zeros((400, 400, 3), dtype=np.uint8)

center = (200, 200)

for i in range(5):
    size = 20 + i * 20
    top_left = (center[0] - size // 2, center[1] - size // 2)
    bottom_right = (center[0] + size // 2, center[1] + size // 2)
    color = (0, 255 - i * 50, 255)
    cv2.rectangle(black_image, top_left, bottom_right, color, 2)

cv2.imwrite('images/squares_loop.jpg', black_image)

cv2.imshow('Squares Loop', black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()