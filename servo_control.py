import time
import serial
import random

ser = serial.Serial('/dev/ttyUSB0', 115200)
time.sleep(2) # wait for servo to initialize

def servo_angle(degrees):
    degrees = int(degrees)
    if degrees == 0: degrees = 1 # arduino parseInt() limitations don't allow to send 0
    ser.write(str(degrees)+"\n")
    ser.flush()
    print(degrees)

servo_angle(90)

def wave_hand():
    global handPos
    handPos = 0
    servo_angle(handPos)
    
    handPos = 90
    servo_angle(handPos)
    time.sleep(0.3)
    
    handPos = 0
    servo_angle(handPos)
    time.sleep(0.3)
    
    handPos = 90
    servo_angle(handPos)
    time.sleep(0.3)
    
    handPos = 0
    servo_angle(handPos)

handPos = 0
def hand_random():
    global handPos
    handPos += random.choice([-25,-20,-15,15,20,25])
    if handPos > 120: handPos = 120
    if handPos < 0: handPos = 0
    servo_angle(handPos)


'''
wave_hand()

for i in range(10):
    hand_random()
    time.sleep(0.2)

wave_hand()

for i in range(10):
    hand_random()
    time.sleep(0.2)
'''


'''
servo_angle(0)
time.sleep(1)

servo_angle(90)
time.sleep(1)

servo_angle(180)
time.sleep(1)

servo_angle(45)
time.sleep(1)
'''

