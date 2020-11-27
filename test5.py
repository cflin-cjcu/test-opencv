import numpy as np
import cv2

img = cv2.imread('test1.jpg')
img[:,100:300,0]=255
img[100:300,:,1]=255
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()