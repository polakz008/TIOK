import cv2

image = cv2.imread('text.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginal", binary)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

eroded_square = cv2.erode(binary, kernel_square, iterations=1)
eroded_ellipse = cv2.erode(binary, kernel_ellipse, iterations=1)

cv2.imshow("Erozja - kwadratowy", eroded_square)
cv2.imshow("Erozja - eliptyczny", eroded_ellipse)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Zwęża się/Chudnie napis