import cv2
import numpy as np

image = cv2.imread("ostre.png")

gauss_noise = np.zeros(image.shape, dtype=np.int16)
cv2.randn(gauss_noise, 0, 25)
noisy_gauss = cv2.add(image.astype(np.int16), gauss_noise)
noisy_gauss = np.clip(noisy_gauss, 0, 255).astype(np.uint8)
cv2.imshow("Obraz z szumem Gaussa", noisy_gauss)
cv2.waitKey(0)

def add_salt_and_pepper_noise(img, amount=0.02):
    noisy = img.copy()
    num_salt = np.ceil(amount * img.size * 0.5).astype(int)
    num_pepper = np.ceil(amount * img.size * 0.5).astype(int)

    coords = [np.random.randint(0, i - 1, num_salt) for i in img.shape[:2]]
    noisy[coords[0], coords[1]] = 255

    coords = [np.random.randint(0, i - 1, num_pepper) for i in img.shape[:2]]
    noisy[coords[0], coords[1]] = 0
    return noisy

noisy_sp = add_salt_and_pepper_noise(image, 0.02)
cv2.imshow("Obraz z szumem soli i pieprzu", noisy_sp)
cv2.waitKey(0)

gauss_blur = cv2.GaussianBlur(noisy_gauss, (5, 5), 0)
cv2.imshow("Gaussian Blur (szum Gaussa)", gauss_blur)
cv2.waitKey(0)

median_blur = cv2.medianBlur(noisy_sp, 5)
cv2.imshow("Median Blur (szum soli i pieprzu)", median_blur)
cv2.waitKey(0)

avg_blur = cv2.blur(noisy_gauss, (5, 5))
cv2.imshow("Average Blur (szum Gaussa)", avg_blur)
cv2.waitKey(0)


bilateral = cv2.bilateralFilter(noisy_gauss, 9, 75, 75)
cv2.imshow("Bilateral Filter (szum Gaussa)", bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()

#
"""
Najlepsze metody:
-Bilateral Blur, Median Blur

"""