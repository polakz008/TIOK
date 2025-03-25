import cv2

image = cv2.imread('image.png')

new_width = image.shape[1] * 3
new_height = image.shape[0] * 3
dim = (new_width, new_height)

methods = [
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

for (name, method) in methods:
    resized = cv2.resize(image, dim, interpolation=method)
    cv2.imshow(f"Metoda: {name}", resized)

cv2.imshow("Oryginalny obraz", image)

cv2.waitKey(0)
cv2.destroyAllWindows()