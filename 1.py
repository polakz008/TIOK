import cv2
import numpy as np

width, height = 400, 400

def draw_triangle(position=(100, 100)):
    mask = np.zeros((height, width), dtype=np.uint8)
    triangle_cnt = np.array([
        [position[0], position[1]],
        [position[0] + 100, position[1] + 150],
        [position[0] - 100, position[1] + 150]
    ])
    cv2.drawContours(mask, [triangle_cnt], 0, 255, -1)
    return mask

def draw_circle(center=(200, 200), radius=100):
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(mask, center, radius, 255, -1)
    return mask

triangle = draw_triangle(position=(300, 100))
circle = draw_circle(center=(200, 200), radius=100)

bitwise_and = cv2.bitwise_and(triangle, circle)
bitwise_or = cv2.bitwise_or(triangle, circle)
bitwise_xor = cv2.bitwise_xor(triangle, circle)
bitwise_not_triangle = cv2.bitwise_not(triangle)

cv2.imshow("Triangle", triangle)
cv2.imshow("Circle", circle)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("XOR", bitwise_xor)
cv2.imshow("NOT Triangle", bitwise_not_triangle)

cv2.waitKey(0)
cv2.destroyAllWindows()
