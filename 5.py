import cv2
import imutils

image = cv2.imread('image.png')

resized = imutils.resize(image, width=500)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Zmieniona szerokosc", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()