import cv2

image_path = 'images/face.png'
image = cv2.imread(image_path)

height, width, _ = image.shape

left_eye = (int(width * 0.40), int(height * 0.35))
right_eye = (int(width * 0.65), int(height * 0.35))
eye_radius = int(min(width, height) * 0.1)

mouth_top_left = (int(width * 0.4), int(height * 0.5))
mouth_bottom_right = (int(width * 0.65), int(height * 0.6))

face_center = (int(width * 0.5), int(height * 0.4))
face_radius = int(min(width, height) * 0.4)

cv2.circle(image, left_eye, eye_radius, (0, 0, 255), -1)
cv2.circle(image, right_eye, eye_radius, (0, 0, 255), -1)

cv2.rectangle(image, mouth_top_left, mouth_bottom_right, (0, 255, 0), -1)

cv2.circle(image, face_center, face_radius, (255, 0, 0), 3)

cv2.imshow('Edited Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
