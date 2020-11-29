from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
 
 
face_cascade = cv2.CascadeClassifier('data/haarcascade/haarcascade_frontalface_default.xml')
 
def detect_haar(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imwrite('haar.png', img)
 
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("a.dat")
 
def detect_face_landmarks(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)
 
    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)
 
        (x, y, w, h) = face_utils.rect_to_bb(face)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
 
        for (x, y) in shape:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            # 圖像、圓心、半徑、顏色、第五個參數正數為線的粗細，負數則為填滿
 
    cv2.imwrite('face_landmarks.png', img)
 
 
filename = "akb48.jpg"
detect_haar(filename)
detect_face_landmarks(filename)