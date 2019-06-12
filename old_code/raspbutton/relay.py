import RPi.GPIO as GPIO
import time

relayPin = 13
btnPin = 24

relay_status = 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(relayPin, GPIO.HIGH)


def swLed(ev=None):
    global relay_status
    relay_status = not  relay_status
    GPIO.output(relayPin, relay_status)
    if relay_status == 1:
        print 'relay off \n'
    else:
        print 'relay on \n'

def loop():
    GPIO.add_event_detect(btnPin, GPIO.FALLING, callback=swLed, bouncetime=200)
    while True:
        time.sleep(1)

if __name__ == '__main__':
    setup()
    loop()
