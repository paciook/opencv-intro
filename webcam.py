import cv2
import numpy as np

cap = cv2.VideoCapture(0)


kernel = np.ones((5,5), np.uint8)

while True:
	# Read the status of the operation and get the frame
	success, img = cap.read()
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Grayscale
	img_blur = cv2.GaussianBlur(img, (9,9), 0) # Blur
	img_canny = cv2.Canny(img, 130,150) # Edges

	img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
	img_eroded = cv2.erode(img_dialation, kernel, iterations=1)

	img_resized = cv2.resize(img, (300,200))

	img_cropped = img[100:100+300, 400:400+250]

	# Show the frame
	cv2.imshow("Webcam", img_eroded)
	print(img.shape)

	# If q is pressed, exit
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

img.release()
cv2.destroyAllWindows()