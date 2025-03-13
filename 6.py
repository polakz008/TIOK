import cv2

image = cv2.imread('images/image.png')
h, w, _ = image.shape

center_x, center_y = w // 2, h // 2

square_size = 100
half_square = square_size // 2

left = center_x - half_square
top = center_y - half_square
right = center_x + half_square
bottom = center_y + half_square

image[top:bottom, left:right] = (0, 0, 255)

cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


