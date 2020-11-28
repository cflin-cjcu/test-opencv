import cv2 
import numpy as np
img1=cv2.imread('test1.jpg') 
img2=cv2.imread('logo.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 100:cols+100]
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img2gray)
ret, mask = cv2.threshold(img2gray, 0, 200, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask',mask_inv)
# Now black-out the area of logo in ROI
# 取 roi 中与 mask 中不为傥的值对应的像素的值虽其他值为 0
# 注意䦈䭻必刪有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
cv2.imshow('img1_bg',img1_bg)
# 取 roi 中与 mask_inv 中不为傥的值对应的像素的值虽其他值为 0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
cv2.imshow('img2_fg',img2_fg)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 100:cols+100 ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
