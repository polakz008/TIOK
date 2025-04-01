import cv2

image = cv2.imread("image.png")

choice = int(input("Wybierz sposób odbicia (0 – pionowe, 1 – poziome, -1 – oba): "))

if choice in [0, 1, -1]:
    flipped = cv2.flip(image, choice)
    print("Odbicie lustrzane wykonane.")
    cv2.imshow("Obraz po odbiciu", flipped)
else:
    print("Niepoprawny wybór!")

cv2.waitKey(0)
cv2.destroyAllWindows()
