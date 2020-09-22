import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3,120) # Width
cap.set(4,80) # Height

cap.set(10,255) # Brightness

kernel = np.ones((3,3),np.uint8)

while True:
	# Read the status of the operation and get the frame
	success, img = cap.read()
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Grayscale
	img_blur = cv2.GaussianBlur(img, (9,9), 0) # Blur
	img_canny = cv2.Canny(img, 130,150) # Edges

	img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
	img_eroded = cv2.erode(img_dialation, kernel, iterations=1)

	# Show the frame
	cv2.imshow("Webcam", img_eroded)

	# If q is pressed, exit
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

img.release()
cv2.destroyAllWindows()