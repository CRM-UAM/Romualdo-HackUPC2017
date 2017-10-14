import numpy as np
import time
import cv2
import sys
from voz import *

VALOR_UMBRAL=50
UMBRAL=450000

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
  
  #Frames antiguos
  antiguo = None

  #Cargamos el archivo cascade
  rostroCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

  cap = cv2.VideoCapture(0)
  
  cap.set(38, 1)

  cap.set(3,320)
  cap.set(4,240)

  while(True):
      # Capture frame-by-frame
      ret, frame = cap.read()
      
      # Our operations on the frame come here
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      # Difuminado Gaussiano para reducir ruido
      gray = cv2.GaussianBlur(gray,(21,21),0)
      
      if (len(personas_actuales) == 0):
        if (bloqueo(antiguo, gray)):
	    print("hello")
	    antiguo = gray

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
      cv2.imshow('Rostros',frame)
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
    
def bloqueo(antiguo, frame):
  
  if(antiguo==None):
    return
  texto="\"Hey!Hey!Over here!\""
  # Resta absoluta
  resta = cv2.absdiff(antiguo, frame)
  print resta.sum()
  if(resta.sum() > UMBRAL):
    romualdo_says(texto)
    return 1
 
  return 0
  
def mismaPersona(firstPerson, secondPerson):
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



