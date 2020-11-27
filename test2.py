import numpy as np
import cv2

img = cv2.imread('test1.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.imwrite('test2.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

