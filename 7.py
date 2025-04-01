import cv2

image = cv2.imread('image.png')

height, width = image.shape[:2]

row_height = height // 3
col_width = width // 3

for i in range(3):
    for j in range(3):
        part = image[i*row_height:(i+1)*row_height, j*col_width:(j+1)*col_width]
        cv2.imshow(f'Part {i+1}-{j+1}', part)

cv2.waitKey(0)
cv2.destroyAllWindows()

