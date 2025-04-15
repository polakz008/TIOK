import cv2

image = cv2.imread('niepelne.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)
kernelSizes = [(15, 15)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)

    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Zamykanie: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)

    dilation = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow("Dylatacja: ({}, {})".format(kernelSize[0], kernelSize[1]), dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
#Przykład ma odzwierciedlać zamazany, poszarpany napis i może nie powraca do oryginału ,ale zwiększa możliwości odczytu