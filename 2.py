import cv2

image = cv2.imread("osoba.png")

height, width = image.shape[:2]
masked = image.copy()

eye_rect_w, eye_rect_h = 140, 40
center_x = width // 2
center_y = height // 2 - 50

top_left = (center_x - eye_rect_w // 2, center_y - eye_rect_h // 2)
bottom_right = (center_x + eye_rect_w // 2, center_y + eye_rect_h // 2)

cv2.rectangle(masked, top_left, bottom_right, (0, 0, 0), -1)
cv2.imshow("Bez oczu", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
