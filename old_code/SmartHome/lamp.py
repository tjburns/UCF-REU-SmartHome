import RPi.GPIO as GPIO
import time
import os

lampSignalPin = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(lampSignalPin, GPIO.OUT)
    GPIO.output(lampSignalPin, GPIO.LOW)

def lampLoop():
    while True:
        input = raw_input("To turn lamp off:0 \n To turn lamp on: 1 \n To quit: q \n")
        if(input == "0"):
            GPIO.output(lampSignalPin, GPIO.LOW)
            time.sleep(2)
        elif(input == "1"):
            GPIO.output(lampSignalPin, GPIO.HIGH)
            time.sleep(2)
        elif(input == "q"):
            print "Turning off lamp program\n"
            GPIO.output(lampSignalPin, GPIO.LOW)
            GPIO.cleanup()
            os._exit(1)
        else:
            print "Not valid input"

if __name__ == '__main__':
    setup()
    lampLoop()
