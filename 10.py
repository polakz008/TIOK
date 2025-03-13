import cv2
import numpy as np

image = cv2.imread('images/image.png')

if image is None:
    print("Błąd: Nie udało się załadować obrazu. Sprawdź ścieżkę.")
else:

    b1, g1, r1 = image[50, 50]
    b2, g2, r2 = image[200, 200]

    diff_b = np.abs(np.subtract(b1, b2))
    diff_g = np.abs(np.subtract(g1, g2))
    diff_r = np.abs(np.subtract(r1, r2))

    diff_b = np.clip(diff_b, 0, 255)
    diff_g = np.clip(diff_g, 0, 255)
    diff_r = np.clip(diff_r, 0, 255)

    print(f'Różnica w kanale niebieskim: {diff_b}')
    print(f'Różnica w kanale zielonym: {diff_g}')
    print(f'Różnica w kanale czerwonym: {diff_r}')

    print(f'Piksel w (50, 50) - Red: {r1}, Green: {g1}, Blue: {b1}')
    print(f'Piksel w (200, 200) - Red: {r2}, Green: {g2}, Blue: {b2}')
