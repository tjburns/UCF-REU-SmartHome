import RPi.GPIO as GPIO
import time
import os

motorPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin, GPIO.OUT)

print "l = move to the left"
print "r = move to the right"
print "m = move to the middle"
print "t = test sequence"
print "q = stop and exit"

while True:
    Servo = GPIO.PWM(24, 50)
    Servo.start(2.5)

    input = raw_input("Selection: ")
    if(input == "t"):
        print "move to the center position:"
        Servo.ChangeDutyCycle(7.5)
        time.sleep(1)
        print "move to the right position:"
        Servo.ChangeDutyCycle(12.5)
        time.sleep(1)
        print "move to the left position:"
        Servo.ChangeDutyCycle(2.5)
        time.sleep(1)
        print "Move back to start position."
        Servo.stop()
    if(input == "r"):
        steps = raw_input("steps (1 - 10): ")
        print steps, "steps to the right"
        stepslength = 12.5 / int(steps)
        for Counter in range(int(steps)):
            Servo.ChangeDutyCycle(stepslength * (Counter + 1))
            print stepslength * (Counter + 1)
            time.sleep(0.5)
        time.sleep(1)
        print "Move back to start position"
        Servo.stop()
    elif(input == "m"):
        print "Move back to the center position."
        Servo.start(7.5)
        time.sleep(1)
        print "Move back to start position"
        Servo.stop()
    elif(input == "l"):
        print "Move to the max right position and then to the left position."
        Servo.start(12.5)
        steps = raw_input("steps (1 - 10): ")
        print steps, "steps to the right"
        stepslength = 12.5 / int(steps)
        for Counter in range(int(steps)):
            Servo.ChangeDutyCycle(12.5 - (stepslength * (Counter + 1)))
            print (12.5 - (stepslength * (Counter + 1)))
            time.sleep(0.5)
        time.sleep(1)
        print "Move back to start position"
        Servo.stop()
    elif(input == "q"):
        print "stop the program and exit..."
        os._exit(1)
        Servo.stop()
        GPIO.cleanup()
    else:
        print "not valid"
