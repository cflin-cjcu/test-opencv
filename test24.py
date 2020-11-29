import cv2
import dlib
import imutils

detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('a.dat')
img = cv2.imread('akb.jpg')

faces = detector(img,0)
if (len(faces) > 0):
    for k,d in enumerate(faces):
        cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()),(255,255,255))
        shape = landmark_predictor(img,d)
        for i in range(68):
            cv2.circle(img, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
            cv2.putText(img,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))
cv2.imshow('Frame',img)
cv2.waitKey(0)