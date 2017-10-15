import reconocimiento
import romualdo_says
import servo_test
import mic
import reconocimiento.Persona


class Controller:

  peopleOnCamera = []
  peopleAll = []

  def init():   
    peopleAll=loadDataBase()
    reconocimiento.reconocer(self, peopleOnCamera, peopleAll)

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


def newUsersDatabase ():
    peopleAll.append(peopleOnCamera) # Add all recognize people
    pickle.dump(peopleAll,open('save.p','wb'))

def newUser (name, picture):
    return Persona(name,picture)


def loadDataBase:
    # Check possible users database
    try:
        database=pickle.load(open('save.p','rb'))
            
        print('Users loaded: %d' % database.length())
        return database

    except IOError:
        print('No database!')


if __name__ == "__main__":
    Controller.init()