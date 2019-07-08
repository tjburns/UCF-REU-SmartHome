import RPi.GPIO as GPIO
import time
import os
import Adafruit_DHT
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# Dictionary containing named doors and windows and their respective pins
motor_names = {1:'front door', 2:'living-bedroom1 door', 3:'living-bathroom door', 4:'living-kitchen door', 5:'bed1-bathroom door', 6:'bed2-bathroom door', 7:'back door', 					8:'living window1', 9:'living window2', 10:'bedroom1 window1', 11:'bedroom1 window2', 12:'bedroom2 window1', 13:'bedroom2 window2', 14:'dining window',0:'kitchen window'}
motor_states = {0:'closed', 1:'closed', 2:'closed', 3:'closed', 4:'closed', 5:'closed', 6:'closed', 7:'closed', 
				8:'closed', 9:'closed', 10:'closed', 11:'closed', 12:'closed', 13:'closed', 14:'closed', 15:'closed'}


# LAMP

def turnOffLamp(pin):
	GPIO.output(pin, GPIO.LOW)
	
def turnOnLamp(pin):
	GPIO.output(pin, GPIO.HIGH)
	
#FAN

def turnOffFan(pin):
	GPIO.output(pin, GPIO.LOW)
	
def turnOnFan(pin):
	GPIO.output(pin, GPIO.HIGH)

# WINDOWS/DOORS

def motorOpen(pin):
	#doors
    if(pin == 0):
        kit.servo[pin].angle = 180
    elif(pin == 1):
        kit.servo[pin].angle = 180
    elif(pin == 2):
        kit.servo[pin].angle = 180
    elif(pin == 3):
        kit.servo[pin].angle = 180
    elif(pin == 4):
        kit.servo[pin].angle = 180
    elif(pin == 5):
        kit.servo[pin].angle = 180
    elif(pin == 6):
        kit.servo[pin].angle = 180
    #windows
    elif(pin == 8):
        kit.servo[pin].angle = 180
    elif(pin == 9):
        kit.servo[pin].angle = 180
    elif(pin == 10):
        kit.servo[pin].angle = 180
    elif(pin == 11):
        kit.servo[pin].angle = 170
    elif(pin == 12):
        kit.servo[pin].angle = 180
    elif(pin == 13):
        kit.servo[pin].angle = 165
    elif(pin == 14):
        kit.servo[pin].angle = 180
    elif(pin == 15):
        kit.servo[pin].angle = 159
    else:
        kit.servo[pin].angle = 180
		
def motorClose(pin):
	#doors
    if(pin == 0):
        kit.servo[pin].angle = 60
    elif(pin == 1):
        kit.servo[pin].angle = 57
    elif(pin == 2):
        kit.servo[pin].angle = 55
    elif(pin == 3):
        kit.servo[pin].angle = 70
    elif(pin == 4):
        kit.servo[pin].angle = 60
    elif(pin == 5):
        kit.servo[pin].angle = 60
    elif(pin == 6):
        kit.servo[pin].angle = 62
    #windows
    elif(pin == 8):
        kit.servo[pin].angle = 65
    elif(pin == 9):
        kit.servo[pin].angle = 56
    elif(pin == 10):
        kit.servo[pin].angle = 69
    elif(pin == 11):
        kit.servo[pin].angle = 60
    elif(pin == 12):
        kit.servo[pin].angle = 47
    elif(pin == 13):
        kit.servo[pin].angle = 56
    elif(pin == 14):
        kit.servo[pin].angle = 60
    elif(pin == 15):
        kit.servo[pin].angle = 46
    else:
        kit.servo[pin].angle = 60
		
# Methods assume the pin in use has been setup

def openAllDoors():
	for pin in range(0,7):
		motorOpen(pin)

def closeAllDoors():
	for pin in range(0,7):
		motorClose(pin)

def openAllWindows():
	for pin in range(7,16):
		motorOpen(pin)

def closeAllWindows():
	for pin in (7,16):
		motorClose(pin)

def openAll():
	openAllDoors()
	openAllWindows()

def closeAll():
	closeAllDoors()
	closeAllWindows()
