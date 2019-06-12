import RPi.GPIO as GPIO
import time
import os

motorPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin, GPIO.OUT)

print "left = move to the left"
print "right = move to the right"
print "center = move to the middle"
print "q = stop and exit"

while True:
    Servo = GPIO.PWM(24, 30)
    Servo.start(2.5)

    input = raw_input("Selection: ")
    if(input == "c"):
        print("Moving to center")
        Servo.start(7.5)
        time.sleep(1)
    elif(input == "r"):
        print("Moving 180 degrees to the right")
        Servo.start(12.5)
        time.sleep(1)
    elif(input == "l"):
        print("Moving 180 degrees to the left")
        Servo.start(2.5)
        time.sleep(1)
    elif(input == "q"):
        print "Stopping motor program..."
        os._exit(1)
        Servo.stop()
        GPIO.cleanup()
