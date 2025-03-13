import cv2

image = cv2.imread('images/image.png')
cv2.imshow('Original Image', image)

image[50:100, 50:100] = (255, 255, 255)

cv2.imshow('Modified Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

