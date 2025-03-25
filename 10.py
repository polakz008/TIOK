import cv2
import imutils

image = cv2.imread('image.png')

resized = imutils.resize(image, width=800)

cv2.imwrite('resized_output.jpg', resized)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Powiekszony obraz", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
