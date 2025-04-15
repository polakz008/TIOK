import cv2

image = cv2.imread('text.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginalny obraz", binary)


kernel_shapes = {
    "Kwadrat": cv2.MORPH_RECT,
    "Elipsa": cv2.MORPH_ELLIPSE,
    "Krzyz": cv2.MORPH_CROSS
}

kernel_size = (7, 7)

for shape_name, shape_type in kernel_shapes.items():
    kernel = cv2.getStructuringElement(shape_type, kernel_size)

    eroded = cv2.erode(binary, kernel)
    dilated = cv2.dilate(binary, kernel)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow(f"Erozja - {shape_name}", eroded)
    cv2.imshow(f"Dylatacja - {shape_name}", dilated)
    cv2.imshow(f"Otwarcie - {shape_name}", opened)
    cv2.imshow(f"Zamkniecie - {shape_name}", closed)
    cv2.imshow(f"Gradient - {shape_name}", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Nie zauważam różnic przy zmianie kształtu przy rozmiarze 5x5, natomiast gdy już zwiększam do 7x7 to elpisa zaokrągla, krzyż tak pixeluje, a kwadrat wyostrza.