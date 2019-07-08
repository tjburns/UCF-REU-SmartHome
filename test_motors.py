import RPi.GPIO as GPIO
import time
import os
import Adafruit_DHT
from adafruit_servokit import ServoKit

from pin_control import *
from sequences import *

		
if __name__ == '__main__':
	#print('setting up pins')
	#setupALL()
	
	#openAllWindows()
	#openAllDoors()
	#closeAllWindows()
	#closeAllDoors()
    
        closeAll()
        while True:
            
            sequence_random()
            
            print()
            for i in range(0,30):
                #print('Next action in: ' + str(i)+'/300', flush=True)
                time.sleep(1)

		
        """
	try:
		while True:
			print('Enter desired operation')
			op = input().lower()
			words = op.split()
			if op == 'open all':
				print("opening all doors and windows")
				openAll()
			elif op == 'close all':
				print("closing all doors and windows")
				closeAll()
			elif op == 'open all doors':
				print("opening all doors")
				openAllDoors()
			elif op == 'close all doors':
				print("closing all doors")
				closeAllDoors()
			elif op == 'open all windows':
				print("opening all windows")
				openAllWindows()
			elif op == 'close all windows':
				print("closing all windows")
				closeAllWindows()
			elif words[0] == 'open':
				#open based on pin number
				print("opening " + motor_names[int(words(1))])
				motorOpen(int(words[1]))
			elif words[0] == 'close':
				#close based on pin number
				print("closing " + motor_names[int(words(1))])
				motorOpen(int(words[1]))
			else:
			    print('Incorrect input.')
	
	except KeyboardInterrupt:
		print("Keyboard interrupt.")
	except Exception as e: 
		print(e)
	finally:
		GPIO.cleanup()
		"""
