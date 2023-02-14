
from tkinter import filedialog as fd
filename1 = fd.askopenfilename()

from tkinter import filedialog as fd
filename2 = fd.askopenfilename()

import cv2
import face_recognition
 
imgTRAIN = face_recognition.load_image_file(filename1)
imgTRAIN = cv2.cvtColor(imgTRAIN,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file(filename2)
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(imgTRAIN)[0]
encodeTRAIN = face_recognition.face_encodings(imgTRAIN)[0]
cv2.rectangle(imgTRAIN,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
 
results = face_recognition.compare_faces([encodeTRAIN],encodeTest)
faceDis = face_recognition.face_distance([encodeTRAIN],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
 
cv2.imshow("TRAIN",imgTRAIN)
cv2.imshow('TEST',imgTest)
cv2.waitKey(0)

