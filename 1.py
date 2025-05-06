import cv2

image = cv2.imread("kotek.png")
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernelSizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow(f"Average Blur ({kX}, {kY})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow(f"Gaussian Blur ({kX}, {kY})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()


for k in [3, 9, 15]:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median Blur (k={k})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()


bilateralParams = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for (diameter, sigmaColor, sigmaSpace) in bilateralParams:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = f"Bilateral Blur d={diameter}, sc={sigmaColor}, ss={sigmaSpace}"
    cv2.imshow(title, blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

#
"""
Która metoda najlepiej usuwa szum?
- Gaussian Blur ma najlepszy efekt rozmycia

Która metoda zachowuje najwięcej szczegółów?
- Bilateral Filter

Zalety i wady każdej metody:
1. Average Blur:
   + Zaleta: szybka 
   - Wada: mocno rozmywa krawędzie i szczegóły

2. Gaussian Blur:
   + Zaleta: lepsze zachowanie krawędzi niż Average
   - Wada: mocno rozmywa szczegóły

3. Median Blur:
   + Zaleta: skuteczna w usuwaniu szumu 
   - Wada: rozmywa szczegóły w plamy kolorów

4. Bilateral Filter:
   + Zaleta: zachowuje krawędzie
   - Wada: wolniejszy
"""
