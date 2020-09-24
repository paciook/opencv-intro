import cv2
import numpy as np
def empty(a):
	pass

path = 'imgs/naipe.jpg'

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640,480)

cv2.createTrackbar("Hue min", "Trackbar", 0,179,empty)
cv2.createTrackbar("Hue max", "Trackbar", 179 ,179,empty)
cv2.createTrackbar("Sat min", "Trackbar", 0,255,empty)
cv2.createTrackbar("Sat max", "Trackbar", 255,255,empty)
cv2.createTrackbar("Val min", "Trackbar", 0,255,empty)
cv2.createTrackbar("Val max", "Trackbar", 255,255,empty)




while True:

	img = cv2.imread(path)

	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	h_min = cv2.getTrackbarPos("Hue min", "Trackbar")
	h_max = cv2.getTrackbarPos("Hue max", "Trackbar")
	s_min = cv2.getTrackbarPos("Sat min", "Trackbar")
	s_max = cv2.getTrackbarPos("Sat max", "Trackbar")
	v_min = cv2.getTrackbarPos("Val min", "Trackbar")
	v_max = cv2.getTrackbarPos("Val max", "Trackbar")

	
	lower = np.array([h_min,s_min,v_min])
	upper = np.array([h_max,s_max,v_max])

	mask = cv2.inRange(imgHSV,lower,upper)

	cv2.imshow("Img", imgHSV)
	cv2.imshow("Mask", mask)

cv2.destroyAllWindows()

