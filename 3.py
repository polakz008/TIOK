import cv2
image = cv2.imread('szum.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginalny obraz z szumem", binary)

kernel_sizes = [(3, 3), (5, 5), (7, 7)]

for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Otwarcie: kernel {size[0]}x{size[1]}", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Najlepsza skuteczność w ostatnim wyniku.