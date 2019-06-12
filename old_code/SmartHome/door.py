import RPi.GPIO as GPIO
import time
import os

lampSignalPin = 25

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(lampSignalPin, GPIO.OUT)
    GPIO.output(lampSignalPin, GPIO.LOW)

def lampLoop():
    while True:
        input = raw_input("To open the window: o \n To close the window: c\n To stop the program: Any key \n")
        if(input == "o"):
	    start = time.time()
            now = time.time()
	    duty = 0.001 + 0.0001*float(2)	
	    while now-start < 1:
            	GPIO.output(lampSignalPin, GPIO.HIGH)
	    	time.sleep(duty)
	    	GPIO.output(lampSignalPin, GPIO.LOW)	
            	time.sleep(0.02-duty)
		now = time.time()
        elif(input == "c"):
            start = time.time()
            now = time.time()
	    duty = 0.001 + 0.0001*float(16)	
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
