import RPi.GPIO as GPIO
import time
import os

from pin_control import *
#from sequences import *

		
if __name__ == '__main__':
	print('setting up pins')
	setupALL()
	
	
	#openAllWindows()
	#openAllDoors()
	#closeAllWindows()
	#closeAllDoors()
	
	#sequence_random()
	
	try:
		while True:
			print('Enter desired operation')
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
			elif words[0] == 'open':
				#open based on pin number
				motorOpen(int(words[1]))
			elif words[0] == 'close':
                            #close based on pin number
				motorOpen(int(words[1]))
			else:
			    print('Incorrect input.')
	
	except KeyboardInterrupt:
		print("Keyboard interrupt.")
	except Exception as e: 
		print(e)
	finally:
		GPIO.cleanup()
