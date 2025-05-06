import cv2

image = cv2.imread("kotek.png")
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernelSizes = [3, 5, 9, 15]

for k in kernelSizes:
    blurred = cv2.blur(image, (k, k))
    cv2.imshow(f"Average Blur ({k}x{k})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

for k in kernelSizes:
    blurred = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f"Gaussian Blur ({k}x{k})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()

for k in kernelSizes:
    if k % 2 == 1:
        blurred = cv2.medianBlur(image, k)
        cv2.imshow(f"Median Blur (k={k})", blurred)
        cv2.waitKey(0)
cv2.destroyAllWindows()


for k in kernelSizes:
    sigmaColor = k * 3
    sigmaSpace = k * 2
    blurred = cv2.bilateralFilter(image, d=k, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
    cv2.imshow(f"Bilateral Blur (d={k}, sc={sigmaColor}, ss={sigmaSpace})", blurred)
    cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
 Im większy kernel, tym silniejsze rozmycie.

Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
- Average Blur:  3x3 lub 5x5 
- Gaussian Blur: 5x5 lub 9x9 
- Median Blur: 3 lub 5
- Bilateral Filter: d=9–11, sigmaColor=27–33, sigmaSpace=18–22 

"""
