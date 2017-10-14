
import numpy as np
import time
import cv2
from skimage.measure import compare_ssim
import argparse
import imutils


VALOR_UMBRAL=50

userlist=[]

class Coordenadas:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Persona:
	def __init__(self, name, picture)
		self.name = name
		self.picture = picture

def reconocer():
	
	
	#Espacio de coordenadas
	coordenadas = []
	
	#Frames de personas actuales
	personas_actuales = []
	
	personas_abandono = []
	
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
		n_rostros = len(rostros)
		actualizarPersona(rostros, personas_actuales, personas_abandono)
		
		for (x, y, w, h) in rostros:

			i = actualizarPosicion(x, y, coordenadas, n_rostros)
			if (i == None):
				continue

			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			cv2.imshow('Tu face'+str(i),frame[y:y+h, x:x+w])
		
			# Display the resulting frame
			#cv2.imshow('Rostros',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

	exit()


def actualizarPosicion(x,y, coordenadas, n_rostros):
	for coord in coordenadas:
		r1 = x - coord.x
		r2 = y - coord.y
		if ( abs(r1) < VALOR_UMBRAL and abs(r2) < VALOR_UMBRAL ):
			coord.x=x
			coord.y=y
			return coordenadas.index(coord)

	if (n_rostros == len(coordenadas)):
		return None
	
	coord=Coordenadas(x,y)
	coordenadas.append(coord)
			
	return coordenadas.index(coord)

def actualizarPersona(rostros, personas_actuales, personas_abandono):
	auxiliar=None
	for p_a in personas_actuales:
		for r in rostros:
			if (mismaPersona(p_a, r) == True):
				auxiliar=None
				break
			else:
				auxiliar = p_a

		persona_saliendo = personas_actuales.pop(personas_actuales.index(auxiliar))
		personas_abandono.append(persona_saliendo)
		
def isNewPerson(possibleNewPerson)
	for i in userlist:
		mismaPersona
	
def mismaPersona(firstPerson, secondPerson):
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-f", "--first", required=True, help="first input image")
	ap.add_argument("-s", "--second", required=True, help="second")
	args = vars(ap.parse_args())
	
	return True

def newUsersDatabase ():
    f=open('database.txt','w')
    print('New database created!')
    f.close()

def newUser (name, picture):
    return Persona(name,picture)

if __name__ == "__main__":
	# Check possible users database
    try:
        database=open('database.txt','r')

        cont=0
        for line in database:
            data=line.split(' ')
            userlist.append(newUser(data[0],data[1]))
            cont+=1
            
        print('Load users: %d' % cont)
        database.close()

    except IOError:
        print('No database, creating...')
        newUsersDatabase()

	reconocer()



