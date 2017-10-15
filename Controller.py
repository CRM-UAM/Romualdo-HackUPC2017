import reconocimiento
import romualdo_says
import servo_test
import mic

class Controller:

  peopleOnCamera = []
  peopleAll = []

  def movementDetected():
    romualdo_says.romualdo_says("HEY YOU!")
    servo_test.servo_angle(1)

  def someoneLooksAtMe(person):
    print('me miran')
    #TODO: comprobar si la conocemos
    #Saludar
    #Anadir a activos


  def someoneLeaves(person):
    print('se piran')
    #TODO: si la conocemos, adios Paco!
