import RPi.GPIO as GPIO
import time
import os
import Adafruit_DHT

# Dictionary containing named doors and windows and their respective pins
motor_names = {1:'front door', 2:'living-bedroom1 door', 3:'living-bathroom door', 4:'living-kitchen door', 5:'bed1-bathroom door', 6:'bed2-bathroom door', 7:'back door', 					8:'living window1', 9:'living window2', 10:'bedroom1 window1', 11:'bedroom1 window2', 12:'bedroom2 window1', 13:'bedroom2 window2', 14:'dining window',0:'kitchen window'}
motor_states = {1:'closed', 2:'closed', 3:'closed', 4:'closed', 5:'closed', 6:'closed', 7:'closed', 
				8:'closed', 9:'closed', 10:'closed', 11:'closed', 12:'closed', 13:'closed', 14:'closed', 15:'closed', 0:'closed'}

# SETUP PINS

def setup():
	GPIO.setmode(GPIO.BCM)
	
def setupPin(pin):
	GPIO.setup(pin, GPIO.OUT)
	# this line might not be necessary
	GPIO.output(pin, GPIO.LOW)

def setupDoorsAndWindows():
	setup()
	for pin in motor_states:
		setupPin(int(pin))

def setupALL():
	setup()
	setupDoorsAndWindows()

# HUMIDITY/TEMPERATURE SENSOR

def getHumidityAndTemperature(pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity > 100:
        return -1, -1
    elif humidity is not None and temperature is not None:
        temp = (temperature * 9.0 / 5.0) + 32
        return temp, humidity
    else:
        return -1, -1

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
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(2)
	while now-start < 1:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(pin, GPIO.LOW)	
		time.sleep(0.02-duty)
		now = time.time()
		
def motorClose(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(-7)	
	while now-start < 1:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(0.02-duty)
		now = time.time()
		
# Methods assume the pin in use has been setup

def openAllDoors():
	for pin in range(0,7):
		motorOpen(pin)

def closeAllDoors():
	for pin in range(0,7):
		motorClose(pin)

def openAllWindows():
	for pin in range(7,15):
		motorOpen(pin)

def closeAllWindows():
	for pin in (7,15):
		motorClose(pin)

def openAll():
	openAllDoors()
	openAllWindows()

def closeAll():
	closeAllDoors()
	closeAllWindows()
