import cv2
import numpy as np
#mouse callback function
def draw_circle(event,x,y,flags,param):
    
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img1,(x,y),100,(255,0,0),-1)
# 创建图像与窗口并将窗口与回䖲函数绑定
img=np.zeros((512,512,3),np.uint8)
print(img)
img1=np.full((512,512,3),np.uint8(255))
print(img1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img1)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()