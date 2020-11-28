import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('test10.jpg')
rows,cols,ch=img.shape
pts1 = np.float32([[116,587],[60,219],[622,89],[717,492]])
pts2 = np.float32([[0,0],[300,0],[300,300],[0,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))
dst1 = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst1), plt.title('Output')
plt.show()