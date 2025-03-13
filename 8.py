import cv2

image = cv2.imread('images/image.png')
cv2.imshow('Original Image', image)

image[99, :, :] = (0, 255, 0)

cv2.imshow('Modified Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

