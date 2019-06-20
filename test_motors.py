import RPi.GPIO as GPIO
import time
import os

from pin_control.py import *

def 
		
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
