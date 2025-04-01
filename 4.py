import cv2

image = cv2.imread("image.png")

filtered_image = image.copy()
filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 30)
filtered_image[:, :, 1] = cv2.subtract(filtered_image[:, :, 1], 20)
filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 10)

cv2.imshow("Original", image)
cv2.imshow("Instagram", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
