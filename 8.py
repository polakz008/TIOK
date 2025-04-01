import cv2

image = cv2.imread('image.png')
roi_width, roi_height = 100, 100
height, width = image.shape[:2]

startX = 0

while startX + roi_width <= width:
    roi = image[:, startX:startX+roi_width]
    cv2.imshow('Przesuwający się ROI', roi)

    key = cv2.waitKey(0)
    if key == 27:
        break
    startX += 10

cv2.destroyAllWindows()
