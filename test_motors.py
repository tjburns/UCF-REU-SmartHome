import RPi.GPIO as GPIO
import time
import os

from pin_control.py import openWindow, openDoor, closeWindow, closeDoor

# Dictionary containing named doors and windows and their respective pins
doors = {'front':2, 'living_bed1':3, 'living_bath':4, 'living_kitchen':17, 'bed1_bath':27, 'bed2_bath':22, 'back':10}
windows = {'living1':9, 'living2':11, 'bed1_1':14, 'bed1_2':15, 'bed2_1':18, 'bed2_2':23, 'dining':24, 'kitchen':25}

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
		
if __name__ == '__main__':
	setupALL():
	
	openAllWindows()
	openAllDoors()
	closeAllWindows()
	closeAllDoors()
	
	try:
		while True:
			op = input().lower()
			words = op.split()
			if op == 'open all':
				openAll()
			elif op == 'close all':
				closeAll()
			elif op == 'open all doors':
				openAllDoors()
			elif op == 'close all doors':
				closeAllDoors()
			elif op == 'open all windows':
				openAllWindows()
			elif op == 'close all windows':
				closeAllWindows()
			elif word[0] == 'open':
				if word[1] == 'door':
					openDoor(doors[word[2]])
				elif word[1] == 'window':
					openWindow(windows[word[2]])
				else
					print('Incorrect input.')
			elif word[0] == 'close':
				if word[1] == 'door':
					closeDoor(doors[word[2]])
				elif word[1] == 'window':
					closeWindow(windows[word[2]])
				else
					print('Incorrect input.')
			else
				print('Incorrect input.')
	
	except KeyboardInterrupt:
        print("Keyboard interrupt.")
    except Exception as e: 
    	print(e)
    finally:
        GPIO.cleanup()
