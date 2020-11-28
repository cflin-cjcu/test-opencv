import cv2
import numpy as np
img=cv2.imread('test1.jpg')
rows, cols=img.shape[:2]
# 下儑的 None 本应䖔是䥂出图像的尺寸虽但是因为后䥨我们䕭置了缩放因子
# 放大
#res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#dst=cv2.resize(img,None,fx=1/2,fy=1/2,interpolation=cv2.INTER_CUBIC)
# 平移
#M = np.float32([[1,0,100],[0,1,50]])
#dst = cv2.warpAffine(img,M,(cols,rows))
#旋轉
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

while(1):
    cv2.imshow('res',dst)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()