import cv2
import time 
import numpy as np
img1=cv2.imread('test1.jpg') 
img2=cv2.imread('logo.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 100:cols+100]
for i in range(100):
    time.sleep(0.1)
    print(i)
    dst=cv2.addWeighted(roi,0.1+i*0.01,img2,0.9-i*0.01,0)
    img1[0:rows, 100:cols+100 ] = dst
    cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
