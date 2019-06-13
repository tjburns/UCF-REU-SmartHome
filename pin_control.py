import RPi.GPIO as GPIO
import time
import os

# Methods assume the pin in use has been setup

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
	GPIO.output(lampSignalPin, GPIO.LOW)
	
def turnOnLamp(pin):
	GPIO.output(lampSignalPin, GPIO.HIGH)
	
#FAN

def turnOffFan(pin):
	GPIO.output(lampSignalPin, GPIO.LOW)
	
def turnOnFan(pin):
	GPIO.output(lampSignalPin, GPIO.HIGH)

# WINDOWS/DOORS

def openWindow(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(2)
	while now-start < 1:
		GPIO.output(lampSignalPin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(lampSignalPin, GPIO.LOW)	
		time.sleep(0.02-duty)
		now = time.time()
		
def openDoor(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(2)
	while now-start < 1:
		GPIO.output(lampSignalPin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(lampSignalPin, GPIO.LOW)	
		time.sleep(0.02-duty)
		now = time.time()	
		
def closeWindow(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(-7)	
	while now-start < 1:
		GPIO.output(lampSignalPin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(lampSignalPin, GPIO.LOW)
		time.sleep(0.02-duty)
		now = time.time()
		
def closeDoor(pin):
	start = time.time()
	now = time.time()
	duty = 0.001 + 0.0001*float(-7)	
	while now-start < 1:
		GPIO.output(lampSignalPin, GPIO.HIGH)
		time.sleep(duty)
		GPIO.output(lampSignalPin, GPIO.LOW)
		time.sleep(0.02-duty)
		now = time.time()
