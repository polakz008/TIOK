import cv2

image = cv2.imread('image.png')

roi = image[0:100, 0:100]

cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
