
import sys
import glob 
import os
import cv2

# classifiers
face_cascade = cv2.CascadeClassifier('faces.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
count=0
files=glob.glob("*.jpg") 
for file in files:
	image = cv2.imread(file)
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	face_detect = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in face_detect:
	    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
	    fa_gray = gray[y:y+h, x:x+w]
	    fa_color = image[y:y+h, x:x+w]
	    path = '/home/prat/Desktop/ML/EVAL'
	    cv2.imwrite(os.path.join(path , "cropped %s.jpg"%(count)), fa_color)
	    cv2.imwrite("/output/cropped %s.jpg"%(count),fa_color)
	    count=count+1
	    goz_detect = eye_cascade.detectMultiScale(fa_gray)
	    for (ex, ey, ew, eh) in goz_detect :
		cv2.rectangle(fa_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)
	    cv2.imshow('Face & Eye Detection', image )
	    





#cv2.destroyAllWindows()




