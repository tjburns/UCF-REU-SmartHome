import RPi.GPIO as GPIO
import time
import os
import numbers

motorPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin, GPIO.OUT)

Servo = GPIO.PWM(24, 30)
Servo.start(2.5)

while True:
    input = raw_input("Selection: ")
    if(input == "q"):
        print "Stopping motor program..."
        os._exit(1)
        Servo.stop()
        GPIO.cleanup()
    elif(input.isdigit()):
	Servo.start(float(input))
    	time.sleep(3)
    else:
	print("Incorrect input")
	time.sleep(2)
