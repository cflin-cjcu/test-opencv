import numpy as np
import cv2

img = cv2.imread('test1.jpg')
# for i in range(200,300):
#     img[i,200]=[0,0,255]
a = img[100:200,100:200]
img[300:400,300:400]=a
print(img.shape)
print(img.size)
print(img.dtype)
print(img[100,100])
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()