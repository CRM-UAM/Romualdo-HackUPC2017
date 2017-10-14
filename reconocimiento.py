
import numpy as np
import time
import cv2

#Cargamos el archivo cascade
rostroCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)


cap.set(3,320)
cap.set(4,240)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rostros = rostroCascade.detectMultiScale(
	    gray,
	    scaleFactor = 1.3,
	    minNeighbors = 10,
	    minSize= (30,30),
	    flags = cv2.CASCADE_SCALE_IMAGE
    )
    i=0
    for (x, y, w, h) in rostros:
	    i+=1
	    #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	    cv2.imshow('Tu face'+str(i),frame[y:y+h, x:x+w])

    # Display the resulting frame
    #cv2.imshow('Rostros',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

exit()
