import cv2

image = cv2.imread('image.png')

for scale in range(100, 301, 20):
    scale_factor = scale / 100.0
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)
    dim = (new_width, new_height)

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

    cv2.imshow(f"Rozmiar: {scale}%", resized)
    cv2.waitKey(500)

cv2.destroyAllWindows()
