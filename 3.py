import cv2
image = cv2.imread('images/image.png')
(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

(b, g, r) = image[cY, cX]
print("Center Pixel at ({}, {}) - Red: {}, Green: {}, Blue: {}".format(cX, cY, r, g, b))

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
