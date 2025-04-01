import cv2

image = cv2.imread('face.png')

height, width = image.shape[:2]

startX = int(width * 0.28)
endX = int(width * 0.72)
startY = int(height * 0.2)
endY = int(height * 0.74)

cropped_face = image[startY:endY, startX:endX]

cv2.imshow('Przycięta twarz', cropped_face)
cv2.waitKey(0)
cv2.destroyAllWindows()

