import cv2
import numpy as np

image = cv2.imread("osoba.png")

height, width = image.shape[:2]

mask = np.zeros((height, width), dtype="uint8")

rect_w, rect_h = 140, 180
center_x = width // 2-10
center_y = height // 2 -30

top_left = (center_x - rect_w // 2, center_y - rect_h // 2)
bottom_right = (center_x + rect_w // 2, center_y + rect_h // 2)

cv2.rectangle(mask, top_left, bottom_right, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Tylko twarz", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
