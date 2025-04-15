import cv2
image = cv2.imread('text.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

thickness_values = []
iterations_list = list(range(1, 6))

def calculate_thickness(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total_area = sum([cv2.contourArea(c) for c in contours])
    total_perimeter = sum([cv2.arcLength(c, True) for c in contours])
    if total_perimeter == 0:
        return 0
    return total_area / total_perimeter

print("Liczba iteracji | Średnia grubość")
print("-----------------------------------------------")

for i in iterations_list:
    dilated = cv2.dilate(binary, kernel, iterations=i)
    thickness = calculate_thickness(dilated)
    thickness_values.append(thickness)
    print(f"{i:<17} | {thickness:.2f}")
    cv2.imshow(f'Dylatacja - iteracja {i}', dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
