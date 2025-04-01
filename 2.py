import cv2

image = cv2.imread('image.png')

height = image.shape[0]
roi = image[height//2:height, :]

cv2.imshow('Dolna połowa', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

