import cv2

image = cv2.imread('image.png')


startX, startY = 50, 50
endX, endY = startX + 100, startY + 100
height, width = image.shape[:2]
roi = image[startY:endY, startX:endX].copy()
newX, newY = 200, 200
image[newY:newY + 100, newX:newX + 100] = roi

cv2.imshow('Modyfikowany obraz', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
