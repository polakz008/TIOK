import cv2

image = cv2.imread("napis.png")
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

#
"""
Które metody najmocniej rozmywają tekst?
- Average Blur, Median Blur, Gaussian Blur

Które pozwalają zachować jego czytelność?
-Bilateral Blur

"""