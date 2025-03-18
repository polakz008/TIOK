import cv2

image_path = 'images/image.png'
image = cv2.imread(image_path)

height, width, _ = image.shape

center = (width // 2, height // 2)

bottom_right = (width - 1, height - 1)

cv2.line(image, center, bottom_right, (255, 0, 0), 2)

cv2.imwrite('images/image_with_line.jpg', image)

cv2.imshow('Image with Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
