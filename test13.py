import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test5.jpg')
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (11, 11), 0)
edges = cv2.Canny(blurred, 80, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
draw = cv2.drawContours(img1, contours, -1, (0, 255, 0), 5)


plt.subplot(131), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(edges,cmap='gray'), plt.title('Edge Image')
plt.subplot(133), plt.imshow(cv2.cvtColor(draw,cv2.COLOR_BGR2RGB)), plt.title('contour Image')

plt.show()
