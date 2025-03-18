import cv2
import imutils

image = cv2.imread('image.png')
cv2.imshow('Original Image', image)

shifted_imutils = imutils.translate(image, 100, 50)
cv2.imshow('Shifted with imutils', shifted_imutils)

cv2.waitKey(0)
cv2.destroyAllWindows()
