import cv2

image = cv2.imread('text.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Oryginalny obraz", image)

kernel_shapes = {
    "Kwadrat": cv2.MORPH_RECT,
    "Elipsa": cv2.MORPH_ELLIPSE
}

kernel_size = (24, 24)

for name, shape in kernel_shapes.items():
    kernel = cv2.getStructuringElement(shape, kernel_size)
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Zamknięcie - {name}", closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
