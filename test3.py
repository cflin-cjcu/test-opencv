import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test1.jpg')
img1 = cv2.cvtColor(img,cv2.COLOR
plt.imshow(img1)
#plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()