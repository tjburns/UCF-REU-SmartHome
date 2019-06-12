#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

digital= 18

def setup():
	GPIO.cleanup()
        GPIO.setwarnings(False) 
	GPIO.setmode(GPIO.BCM)
        GPIO.setup(digital,GPIO.IN)
        
        
def loop():
	while True:
		signal1=GPIO.input(digital) 
		print(signal1)
		time.sleep(0.5)
		


if __name__ == '__main__':
        setup()
        try:
    # Loop until users quits with CTRL-C
                loop()
	except KeyboardInterrupt:
    # Reset GPIO settings
                GPIO.cleanup()
