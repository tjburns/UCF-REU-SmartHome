import RPi.GPIO as GPIO
import time
import os

fanPin = 23

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fanPin, GPIO.OUT)
    GPIO.output(fanPin, GPIO.LOW)

def lampLoop():
    while True:
        input = raw_input("To turn fan off:0 \n To turn fan on: 1 \n To quit: q \n")
        if(input == "0"):
            GPIO.output(fanPin, GPIO.LOW)
            time.sleep(2)
        elif(input == "1"):
            GPIO.output(fanPin, GPIO.HIGH)
            time.sleep(2)
        elif(input == "q"):
            print "Turning off lamp program\n"
            GPIO.output(fanPin, GPIO.LOW)
            os._exit(1)
            GPIO.cleanup()
        else:
            print "Not valid input"

if __name__ == '__main__':
    setup()
    lampLoop()
