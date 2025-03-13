import cv2
image = cv2.imread('images/image.png')

h, w, _ = image.shape

part_h = h // 3
part_w = w // 3

start_x = part_w
start_y = part_h
end_x = 2 * part_w
end_y = 2 * part_h

center_part = image[start_y:end_y, start_x:end_x]

cv2.imshow('Center Fragment', center_part)
cv2.waitKey(0)
cv2.destroyAllWindows()
