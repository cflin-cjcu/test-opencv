import numpy as np
import cv2

img = cv2.imread('test1.jpg')
# print(img)
cv2.rectangle(img,(100,100),(200,200),(0,255,0),10)
cv2.putText(img,'aaa',(100,90), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.imwrite('test2.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

