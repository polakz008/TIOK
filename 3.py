import cv2

image = cv2.imread("image.png")

flipped = cv2.flip(image, -1)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Obraz po odbiciu lustrzanym względem obu osi", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
