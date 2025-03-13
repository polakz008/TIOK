import cv2

image = cv2.imread('images/image.png')
(h, w) = image.shape[:2]

x = int(input(f"Podaj współrzędną X (0 - {w - 1}): "))
y = int(input(f"Podaj współrzędną Y (0 - {h - 1}): "))

if 0 <= x < w and 0 <= y < h:
    cv2.imshow("Original", image)
    image[y, x] = (0, 0, 0)

    cv2.imshow("Modified", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Podane współrzędne są poza zakresem obrazu.")
