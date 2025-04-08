import cv2

image = cv2.imread('obraz.png')

B, G, R = cv2.split(image)
R = cv2.add(R, 100)
enhanced_image = cv2.merge((B, G, R))
cv2.imshow('', enhanced_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
