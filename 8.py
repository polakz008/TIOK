import cv2

image = cv2.imread('image.png')
cv2.imshow('Original Image', image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M1 = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
rotated1 = cv2.warpAffine(image, M1, (w, h))
M2 = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
rotated2 = cv2.warpAffine(rotated1, M2, (w, h))
M3 = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
rotated_final = cv2.warpAffine(rotated2, M3, (w, h))
cv2.imshow("Sequential Rotation ", rotated_final)

M90 = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
rotated_90 = cv2.warpAffine(image, M90, (w, h))
cv2.imshow("Rotated by 90 Degrees", rotated_90)

cv2.waitKey(0)
cv2.destroyAllWindows()