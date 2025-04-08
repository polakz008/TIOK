import cv2
import numpy as np

image = cv2.imread("kwiaty.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_hsv = np.array([140, 50, 50])
upper_hsv = np.array([170, 255, 255])
mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny", image)
cv2.imshow("Ekstrakcja", result)
cv2.waitKey(0)
cv2.destroyAllWindows()