import reconocimiento
import romualdo_says
import servo_test
import voz
import mic

class Controller:

  peopleOnCamera = []
  peopleAll = []

  def movementDetected():
    romualdo_says.romualdo_says("HEY YOU!")
    servo_test.servo_angle(1)

  def someoneLooksAtMe(person):
    #TODO: comprobar si la conocemos
    #Saludar
    #Anadir a activos


  def someoneLeaves(person):
    #TODO: si la conocemos, adios Paco!
