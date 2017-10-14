
import numpy as np
import time
import cv2

VALOR_UMBRAL=50

class Coordenadas:
  def __init__(self, x, y):
    self.x = x
    self.y = y


def reconocer():
  
  
  #Espacio de coordenadas
  coordenadas = []
  
  #Frames de personas actuales
  personas = []
  
  #Cargamos el archivo cascade
  rostroCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

  cap = cv2.VideoCapture(0)

  cap.set(3,320)
  cap.set(4,240)

  while(True):
      # Capture frame-by-frame
      ret, frame = cap.read()
      
      personas.append(frame)
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

def actualizarPersona():
  pass
  
def personaSeVa():
  pass
  
def mismaPersona(old_persona, new_persona):
  return True

if __name__ == "__main__":
  reconocer()



