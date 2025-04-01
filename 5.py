import cv2

s1 = cv2.imread("s1.png")
s2 = cv2.imread("s2.png")

s2 = cv2.resize(s2, (s1.shape[1], s1.shape[0]))

difference = cv2.absdiff(s1, s2)

cv2.imshow("Original Image 1", s1)
cv2.imshow("Original Image 2", s2)
cv2.imshow("Difference", difference)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Obrazy naszły na siebie oraz są w innych kolorach niż oryginały, wygląda jak trochę jak filtr "negatyw"