import dlib
import cv2
import imutils

# 讀取照片圖檔
img = cv2.imread('test6.jpg')

# 縮小圖片
img = imutils.resize(img, width=1280)

# Dlib 的人臉偵測器
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('../a.dat')
# 偵測人臉
face_rects = detector(img, 0)

# 取出所有偵測的結果
for k, d in enumerate(face_rects):
  x1 = d.left()
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()

  # 以方框標示偵測的人臉
  cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)
  shape = landmark_predictor(img,d)
  for i in range(68):
      cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,0,255), -1, 2)
      cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))

# 顯示結果
cv2.imshow("Face Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()