import cv2

image = cv2.imread('image.png')

dim = (200, 300)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Zmieniony rozmiar", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
