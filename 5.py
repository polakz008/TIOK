import cv2

image = cv2.imread("image.png")

height, width, _ = image.shape

roi = image[:, width // 2:]
flipped_roi = cv2.flip(roi, 1)

image[:, width // 2:] = flipped_roi

cv2.imshow("Zmodyfikowany obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
