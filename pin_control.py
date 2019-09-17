import RPi.GPIO as GPIO
import time
import os
import Adafruit_DHT
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# Each Pulse Width Modulation (PWM) Pin corresponds to a motor
 # PWM 0 - 6 : doors
 # PWM 8 - 15 : windows
 # 00 : Bedroom 2 - Bathroom    | 'bedroom2 - bathroom door'
 # 01 : Bedroom 1 - Living Rm   | 'bedroom1 - living room door'
 # 02 : Living Rm - Kitchen     | 'living room - kitchen door'
 # 03 : Living Rm - Bathroom    | 'living - bathroom door'
 # 04 : Bedroom 1 - Bathroom    | 'bedroom1 - bathroom door'
 # 07 : Living Rm - Front Door  | 'living room front door'
 # 06 : Bedroom 1 - Back Door   | 'bedroom1 back door'
 
 # 08 : Bedroom 1, 2 ft.    | 'bedroom1 - 2ft window'
 # 09 : Living Rm, 2 ft.    | 'living room - 2ft window'
 # 10 : Bedroom 2, 2 ft.    | 'bedroom2 - 2ft window'
 # 11 : Kitchen, 2 ft.      | 'kitchen - 2ft window'
 # 12 : Bedroom 2, 3 ft.    | 'bedroom2 - 3ft window'
 # 13 : Living Rm, 3 ft.    | 'living room - 3ft window'
 # 14 : Kitchen, 3 ft.      | 'kitchen - 3ft window'
 # 15 : Bedroom 1, 3 ft.    | 'bedroom1 - 3ft window'

# Dictionary containing named doors and windows and their respective pins
motor_names = {0:'bedroom2 - bathroom door', 1:'bedroom1 - living room door', 2:'living room - kitchen door',
               3:'living - bathroom door', 4:'bedroom1 - bathroom door', 5:'nothing', 6:'bedroom1 back door',
               7:'living room front door', 8:'bedroom1 - 2ft window', 9:'living room - 2ft window', 10:'bedroom2 - 2ft window',
               11:'kitchen - 2ft window', 12:'bedroom2 - 3ft window', 13:'living room - 3ft window', 14:'kitchen - 3ft window',
               15:'bedroom1 - 3ft window'}
motor_names_pinRef =  {'bedroom2 - bathroom door':0, 'bedroom1 - living room door':1, 'living room - kitchen door':2,
                       'living - bathroom door':3, 'bedroom1 - bathroom door':4, 'nothing':5, 'bedroom1 back door':6,
                       'living room front door':7, 'bedroom1 - 2ft window':8, 'living room - 2ft window':9, 'bedroom2 - 2ft window':10,
                       'kitchen - 2ft window':11, 'bedroom2 - 3ft window':12, 'living room - 3ft window':13, 'kitchen - 3ft window':14,
                       'bedroom1 - 3ft window':15}

motor_states = {0:'closed', 1:'closed', 2:'closed', 3:'closed', 4:'closed', 5:'closed', 6:'closed', 7:'closed', 
				8:'closed', 9:'closed', 10:'closed', 11:'closed', 12:'closed', 13:'closed', 14:'closed', 15:'closed'}
motor_states_pinRef = {'bedroom2 - bathroom door':'closed', 'bedroom1 - living room door':'closed', 'living room - kitchen door':'closed', 'living - bathroom door':'closed', 
                        'bedroom1 - bathroom door':'closed', 'nothing':'closed', 'bedroom1 back door':'closed', 'living room front door':'closed', 
                        'bedroom1 - 2ft window':'closed', 'living room - 2ft window':'closed', 'bedroom2 - 2ft window':'closed', 'kitchen - 2ft window':'closed',
                        'bedroom2 - 3ft window':'closed', 'living room - 3ft window':'closed', 'kitchen - 3ft window':'closed', 'bedroom1 - 3ft window':'closed'}


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
	
	motor_states[pin] = 'open'

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
    elif(pin == 7):
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
    	print("ERROR: Pin number out of range")
        kit.servo[pin].angle = 180
		
def motorClose(pin):
	
	motor_states[pin] = 'closed'

	#doors
    if(pin == 0):
        kit.servo[pin].angle = 60
    elif(pin == 1):
        kit.servo[pin].angle = 70
    elif(pin == 2):
        kit.servo[pin].angle = 55
    elif(pin == 3):
        kit.servo[pin].angle = 70
    elif(pin == 4):
        kit.servo[pin].angle = 60
    elif(pin == 7):
        kit.servo[pin].angle = 70
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
    	print("ERROR: Pin number out of range")
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
	for pin in range(7,16):
		motorClose(pin)

def openAll():
	openAllDoors()
	openAllWindows()

def closeAll():
	closeAllDoors()
	closeAllWindows()
