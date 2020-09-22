import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

print(img.shape)

# img[200:300, 230:250] = 255,0,0

cv2.line(img, (0,0), (300,300), (0,255,255), 3)

cv2.rectangle(img, (100,10), (250,300), (0,0,255),cv2.FILLED)

cv2.circle(img, (400,50), 30, (255,255,0), 5)

cv2.putText(img, "PACIOCAPO", (0,200),cv2.FONT_ITALIC,1,(230,230,230),1)

cv2.imshow('img', img)

cv2.waitKey(0)