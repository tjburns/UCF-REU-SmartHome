import RPi.GPIO as GPIO
import time
import os

# Dictionary containing named doors and windows and their respective pins
doors = {'front':2, 'living_bed1':3, 'living_bath':4, 'living_kitchen':17, 'bed1_bath':27, 'bed2_bath':22, 'back':10}
windows = {'living1':9, 'living2':11, 'bed1_1':14, 'bed1_2':15, 'bed2_1':18, 'bed2_2':23, 'dining':24, 'kitchen':25}

# SETUP PINS

def setup():
	GPIO.setmode(GPIO.BCM)
	
def setupPin(pin):
	GPIO.setup(pin, GPIO.OUT)
	# this line might not be necessary
	GPIO.output(pin, GPIO.LOW)

def setupDoors():
	setup()
	for pin in doors.values():
		setupPin(pin)

def setupWindows():
	setup()
	for pin in windows.values():
		setupPin(pin)

def setupALL():
	setup()
	setupDoors()
	setupWindows()

# Methods assume the pin in use has been setup

def openAllDoors():
	for pin in doors.values():
		openDoor(pin)

def closeAllDoors():
	for pin in doors.values():
		closeDoor(pin)

def openAllWindows():
	for pin in windows.values():
		openWindow(pin)

def closeAllWindows():
	for pin in windows.values():
		closeWindow(pin)

def openAll():
	openAllDoors()
	openAllWindows()

def closeAll():
	closeAllDoors()
	closeAllWindows()

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

def openWindow(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(2)
	while now-start < 1:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(pin, GPIO.LOW)	
		time.sleep(0.02-duty)
		now = time.time()
		
def openDoor(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(2)
	while now-start < 1:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(pin, GPIO.LOW)	
		time.sleep(0.02-duty)
		now = time.time()	
		
def closeWindow(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(-7)	
	while now-start < 1:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(0.02-duty)
		now = time.time()
		
def closeDoor(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(-7)	
	while now-start < 1:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(0.02-duty)
		now = time.time()
