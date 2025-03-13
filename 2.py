import cv2
image = cv2.imread('images/image.png')
(h, w) = image.shape[:2]
modified_image = image.copy()
modified_image[h-1, w-1] = (0, 0, 255)

(b, g, r) = modified_image[h-1, w-1]
print("Pixel at ({}, {}) - Red: {}, Green: {}, Blue: {}".format(w-1, h-1, r, g, b))

cv2.imshow("Original", image)
cv2.imshow("Modified", modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()