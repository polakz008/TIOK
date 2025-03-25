import cv2

image = cv2.imread('image.png')

new_width = image.shape[1] * 4
new_height = image.shape[0] * 4
dim = (new_width, new_height)

resized_cubic = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

resized_lanczos = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Powiekszony obraz (INTER_CUBIC)", resized_cubic)
cv2.imshow("Powiekszony obraz (INTER_LANCZOS4)", resized_lanczos)

cv2.waitKey(0)
cv2.destroyAllWindows()
