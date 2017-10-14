import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
time.sleep(2) # wait for servo to initialize

def servo_angle(degrees):
    if degrees == 0: degrees = 1 # arduino parseInt() limitations don't allow to send 0
    ser.write(str(degrees)+"\n")
    ser.flush()

servo_angle(0)
time.sleep(1)

servo_angle(90)
time.sleep(1)

servo_angle(180)
time.sleep(1)

servo_angle(45)
time.sleep(1)


