import reconocimiento
import romualdo_says
import servo_test
import mic
import reconocimiento.Persona


class Controller:

  peopleOnCamera = []
  peopleAll = []

  def init():   
    loadDataBase(peopleAll)
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
    Controller.init()