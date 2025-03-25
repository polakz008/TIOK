import cv2

image = cv2.imread('image.png')
cv2.imshow('Original Image', image)

(h, w) = image.shape[:2]

angle = 30
M = cv2.getRotationMatrix2D((0, 0), angle, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Rotated by 30 Degrees ", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()