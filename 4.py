import cv2

image = cv2.imread("image.png")

flipped_horizontally = cv2.flip(image, 1)
flipped_vertically = cv2.flip(image, 0)
flipped_both = cv2.flip(image, -1)


cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Odbicie poziome", flipped_horizontally)
cv2.imshow("Odbicie pionowe", flipped_vertically)
cv2.imshow("Odbicie względem obu osi", flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
