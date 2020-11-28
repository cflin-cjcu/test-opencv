import cv2
import numpy as np
from matplotlib import pyplot as plt
pts1 = np.float32([[0,0],[0,0],[0,0],[0,0]])
i=0
def savexy(event,x,y,flags,param):
    global pts1
    global i
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        pts1[i]=[x,y]
        i+=1
img=cv2.imread('test10.jpg')
rows,cols,ch=img.shape
pts2 = np.float32([[0,0],[300,0],[300,300],[0,300]])
cv2.namedWindow('image')
cv2.setMouseCallback('image',savexy)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27 or i>3:
        break
cv2.destroyAllWindows()
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))
dst1 = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
plt.subplot(211), plt.imshow(img), plt.title('Input')
plt.subplot(212), plt.imshow(dst1), plt.title('Output')
plt.show()