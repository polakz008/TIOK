import cv2

image = cv2.imread("ostre.png")
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


bilateral_params = [
    (9, 75, 75),
    (9, 150, 150),
    (9, 250, 250)
]

for (d, sc, ss) in bilateral_params:
    blurred = cv2.bilateralFilter(image, d, sc, ss)
    title = f"Bilateral d={d}, sc={sc}, ss={ss}"
    cv2.imshow(title, blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

avg_blur = cv2.blur(image, (9, 9))
cv2.imshow("Average Blur (9x9)", avg_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


gauss_blur = cv2.GaussianBlur(image, (9, 9), 0)
cv2.imshow("Gaussian Blur (9x9)", gauss_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


median_blur = cv2.medianBlur(image, 9)
cv2.imshow("Median Blur (9)", median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#
"""
Czy rozmycie dwustronne skutecznie redukuje szum?
- Tak

Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
- Tak
 
Jakie wartości parametrów dają najlepsze rezultaty?
-d=9, sigmaColor=150, sigmaSpace=150.

"""
