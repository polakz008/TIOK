import cv2

image = cv2.imread('image.png')

width = image.shape[1]
roi = image[:, width//2:width]

cv2.imshow('Prawa połowa', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
