import cv2

image = cv2.imread('image.png')

roi_width, roi_height = 300, 300

height, width = image.shape[:2]

cropped_image = image[0:roi_height, 0:roi_width]

cv2.imwrite('cropped_image.jpg', cropped_image)

cv2.imshow('Przycięty obraz', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
