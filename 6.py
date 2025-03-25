import cv2
import imutils

image = cv2.imread('image.png')
cv2.imshow('Original Image', image)

rotated = imutils.rotate_bound(image, -33)

cv2.imshow("Rotated by -33 Degrees ", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
