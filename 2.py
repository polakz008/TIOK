import cv2

image = cv2.imread('image.png')

new_width = image.shape[1] * 2
new_height = image.shape[0] * 2
dim = (new_width, new_height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Powiekszony obraz", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
