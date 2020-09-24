import cv2
import numpy as np

img = cv2.imread('imgs/naipe.jpg')

width, height = 250,350

pts1 = np.float32([[129,150],[187,128],[244,196],[178,226]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height ]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img, matrix,(width,height))

cv2.imshow("Perspective", imgOutput)

cv2.waitKey(0)
