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
  def __init__(self, name, picture):
    self.name = name
    self.picture = picture


def reconocer(controller, personas_actuales=[], personas_abandono=[]):
  #Espacio de coordenadas
  coordenadas = []
  
  #Frames antiguos
  antiguo = None

  loadDataBase(personas_abandono)

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
      actualizarRostro(rostros,personas_actuales,controller)
      actualizarPersona(rostros, personas_actuales, personas_abandono, controller)
      
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


def nuevoRostro(rostros, personas_actuales,controller):
  auxiliar=set()
  for r in rostro:
    persona_rostro = Persone(None, r)
    for p_a in personas_actuales:
      if (mismaPersona(p_a.picture, r) == True):
	auxiliar.pop(persona_rostro)
	break
      else:
	auxiliar.add(Persona(None,r))
  aux = list(auxiliar)
  personas_actuales.append(aux)
  controller.someoneLooksAtMe(aux)

  


def actualizarPersona(rostros, personas_actuales, personas_abandono,controller):
  auxiliar=set()
  for p_a in personas_actuales:
    for r in rostros:
      if (mismaPersona(p_a.picture, r) == True):
	auxiliar.pop(p_a)
	break
      else:
	auxiliar.add(p_a)

  for aux in auxiliar:
    personas_actuales.pop(personas_actuales.index(aux))
  aux=list(auxiliar)
  personas_abandono.extend(aux)
  controller.someoneLeaves(aux)
    
def bloqueo(antiguo, frame, controller):
  
  if(antiguo==None):
    return
  # Resta absoluta
  resta = cv2.absdiff(antiguo, frame)
  #print resta.sum()
  if(resta.sum() > UMBRAL):
    controller.movementDetected()
    return
 
  return
  
def mismaPersona(firstPerson, secondPerson):
  # compute the Structural Similarity Index (SSIM) between the two
  # images, ensuring that the difference image is returned
  diff = absdiff(firstPerson, secondPerson)

  # threshold the difference image, followed by finding contours to
  # obtain the regions of the two input images that differ
  thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
  cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if imutils.is_cv2() else cnts[1]

  # loop over the contours
  errorArea=0
  for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    # cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    errorArea+=w*h

    if errorArea<0.3*cv2.findContours(firstPerson.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE):
      return True
    else:
      return False


def newUsersDatabase ():
    f=open('database.txt','w')
    print('New database created!')
    f.close()

def newUser (name, picture):
    return Persona(name,picture)


def loadDataBase(personas_abandono):
    # Check possible users database
    try:
        database=open('database.txt','r')

        cont=0
        for line in database:
            data=line.split(' ')
            personas_abandono.append(newUser(data[0],data[1]))
            cont+=1
            
        print('Load users: %d' % cont)
        database.close()

    except IOError:
        print('No database, creating...')
        newUsersDatabase()


if __name__ == "__main__":
    reconocer()



