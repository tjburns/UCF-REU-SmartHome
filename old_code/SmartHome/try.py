import RPi.GPIO as GPIO
import time
import os

lampSignalPin = 21

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(lampSignalPin, GPIO.OUT)
    GPIO.output(lampSignalPin, GPIO.LOW)

def lampLoop():
    while True:
        input = raw_input("To turn lamp off:0 \n To turn lamp on: 1 \n To quit: q \n")
        if(float(input)):
	    start = time.time()
            now = time.time()
	    duty = 0.001 + 0.0001*float(input)	
	    while now-start < 1:
            	GPIO.output(lampSignalPin, GPIO.HIGH)
	    	time.sleep(duty)
	    	GPIO.output(lampSignalPin, GPIO.LOW)	
            	time.sleep(0.02-duty)
		now = time.time()
        else:
            print "Stopping motor program..."
            os._exit(1)
            GPIO.cleanup()

if __name__ == '__main__':
    setup()
    lampLoop()
