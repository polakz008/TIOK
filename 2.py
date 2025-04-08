import cv2

img1 = cv2.imread('bez.png')
img2 = cv2.imread('z.jpg')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

xor_result = cv2.bitwise_xor(gray1, gray2)


cv2.imshow("1", gray1)
cv2.imshow("2", gray2)
cv2.imshow("XOR", xor_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
