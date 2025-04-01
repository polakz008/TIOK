import cv2

image = cv2.imread('image.png')

height, width = image.shape[:2]

startX = int(input(f"Podaj startX (0 - {width-1}): "))
endX = int(input(f"Podaj endX ({startX+1} - {width}): "))
startY = int(input(f"Podaj startY (0 - {height-1}): "))
endY = int(input(f"Podaj endY ({startY+1} - {height}): "))

if not (0 <= startX < endX <= width and 0 <= startY < endY <= height):
    print("Błąd")
    exit()

roi = image[startY:endY, startX:endX]

cv2.imshow('Wybrany ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
