import cv2


image = cv2.imread("opencw.png")
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

cv2.imwrite("red_channel.jpg", R)
cv2.imwrite("green_channel.jpg", G)
cv2.imwrite("blue_channel.jpg", B)

cv2.waitKey(0)
cv2.destroyAllWindows()
