import cv2
import imutils

image = cv2.imread('image.png')

resized = imutils.resize(image, height=400)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Zmieniona wysokosc", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
