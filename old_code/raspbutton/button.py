import RPi.GPIO as GPIO
import time

ledPin = 12
btnPin = 24

led_status = 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(ledPin, GPIO.HIGH)


def swLed(ev=None):
    global led_status
    led_status = not led_status
    GPIO.output(ledPin, led_status)
    if led_status == 1:
        print 'led off \n'
    else:
        print 'led on \n'

def loop():
    GPIO.add_event_detect(btnPin, GPIO.FALLING, callback=swLed, bouncetime=200)
    while True:
        time.sleep(1)

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

