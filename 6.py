import cv2
import numpy as np

image = cv2.imread("truskawka.png")
mask = np.zeros(image.shape[:2], dtype="uint8")

cv2.ellipse(mask, (image.shape[1]//2, int(image.shape[0]*0.70)), (100, 160), 0, 0, 360, 255, -1)

blurred = cv2.GaussianBlur(image, (31, 31), 0)

foreground = cv2.bitwise_and(image, image, mask=mask)
inv_mask = cv2.bitwise_not(mask)
background = cv2.bitwise_and(blurred, blurred, mask=inv_mask)

final = cv2.add(foreground, background)

cv2.imshow("Symulacja głębi ostrości", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
