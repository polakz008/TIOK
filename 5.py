import cv2
import imutils

image = cv2.imread('image.png')
cv2.imshow('Original Image', image)

rotated = imutils.rotate(image, 180)

cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()