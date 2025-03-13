import cv2

image = cv2.imread('images/image.png')

max_brightness = -1
max_brightness_pixel = None
max_brightness_coords = None

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        b, g, r = image[y, x]

        brightness = (float(b) + float(g) + float(r)) / 3

        if brightness > max_brightness:
            max_brightness = brightness
            max_brightness_pixel = (r, g, b)
            max_brightness_coords = (x, y)

print(f'Najjaśniejszy piksel znajduje się na współrzędnych: {max_brightness_coords}')
print(f'Wartość piksela (R, G, B): {max_brightness_pixel}')
