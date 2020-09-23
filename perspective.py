import cv2
import numpy as np

img = cv2.imread('imgs/algo.jpg')

img = cv2.resize(img, (480,640))

cv2.imshow("Imagen", img)

cv2.waitKey(0)