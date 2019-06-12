import RPi.GPIO as GPIO
import time
import os
import Adafruit_DHT
import random
from datetime import datetime

door_one_pin = 25
door_two_pin = 21
window_one_pin = 16
window_two_pin = 20
lamp_pin = 24
fanPin = 23
roomA_pin = 6
roomB_pin = 12
roomC_pin = 26
roomD_pin = 19
outside_pin = 13
sensor=Adafruit_DHT.DHT11

def setup():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(door_one_pin, GPIO.OUT) #set door 1 as output
    GPIO.setup(door_two_pin, GPIO.OUT) #set door 2 as output
    GPIO.setup(window_one_pin, GPIO.OUT) #set window 1 as output
    GPIO.setup(window_two_pin, GPIO.OUT) #set window 2 as output
    GPIO.setup(lamp_pin, GPIO.OUT) #set heating lamp as output
    GPIO.setup(fanPin, GPIO.OUT) #set fan as output
    
    GPIO.output(door_one_pin, GPIO.LOW)
    GPIO.output(door_two_pin, GPIO.LOW)
    GPIO.output(window_one_pin, GPIO.LOW)
    GPIO.output(window_two_pin, GPIO.LOW)
    GPIO.output(lamp_pin, GPIO.LOW)
    GPIO.output(fanPin, GPIO.LOW)

def controlDoorOne(x):
    if(x == "1"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(2)	
        while now-start < 1:
            GPIO.output(door_one_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(door_one_pin, GPIO.LOW)	
            time.sleep(0.02-duty)
            now = time.time()
    elif(x == "0"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(16)
        while now-start < 1:
            GPIO.output(door_one_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(door_one_pin, GPIO.LOW)
            time.sleep(0.02-duty)
            now = time.time()

def controlDoorTwo(x):
    if(x == "1"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(2)	
        while now-start < 1:
            GPIO.output(door_two_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(door_two_pin, GPIO.LOW)	
            time.sleep(0.02-duty)
            now = time.time()
    elif(x == "0"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(20)
        while now-start < 1:
            GPIO.output(door_two_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(door_two_pin, GPIO.LOW)
            time.sleep(0.02-duty)
            now = time.time()

def controlWindowOne(x):
    if(x == "1"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(2)
        while now-start < 1:
            GPIO.output(window_one_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(window_one_pin, GPIO.LOW)
            time.sleep(0.02-duty)
            now = time.time()
    elif(x == "0"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(-7)
        while now-start < 1:
            GPIO.output(window_one_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(window_one_pin, GPIO.LOW)
            time.sleep(0.02-duty)
            now = time.time()

def controlWindowTwo(x):
    if(x == "1"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(2)	
        while now-start < 1:
            GPIO.output(window_two_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(window_two_pin, GPIO.LOW)	
            time.sleep(0.02-duty)
            now = time.time()
    elif(x == "0"):
        start = time.time()
        now = time.time()
        duty = 0.001 + 0.0001*float(-7)
        while now-start < 1:
            GPIO.output(window_two_pin, GPIO.HIGH)
            time.sleep(duty)
            GPIO.output(window_two_pin, GPIO.LOW)
            time.sleep(0.02-duty)
            now = time.time()

def controlLamp(x):
    if(x == "0"):
        GPIO.output(lamp_pin, GPIO.LOW)
    elif(x == "1"):
        GPIO.output(lamp_pin, GPIO.HIGH)

def controlFan(x):
    if(x == "0"):
        GPIO.output(fanPin, GPIO.LOW)
    elif(x == "1"):
        GPIO.output(fanPin, GPIO.HIGH)
    elif(x == "q"):
        GPIO.output(fanPin, GPIO.LOW)
        os._exit(1)
        GPIO.cleanup()
    else:
         print ("Not valid input.")

def getTemp(room):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, room)
    if humidity > 100:
        return -1, -1
    elif humidity is not None and temperature is not None:
        temp = (temperature * 9.0 / 5.0) + 32
        return temp, humidity
    else:
        return -1, -1

if __name__ == '__main__':
    setup()
    message = "To turn the lamp off: L0\n" + "To turn lamp on: L1\n" + "To turn fan off: F0\n" + "To turn fan on: F1\n"
    message += "To open door one: D11\n" + "To close door one: D10\n" + "To open window one: W11\n" + "To close window one: W10\n"
    message += "To open window two: W21\n" + "To close window two: W20\n" + "To close door two: D20\n" + "To open door two: D21\n"

    doorOne_state = 0
    doorTwo_state = 0
    windowOne_state = 0
    windowTwo_state = 0
    lamp_state = 0
    fan_state = 0
    roomA_temp = 0
    roomB_temp = 0
    roomC_temp = 0
    roomD_temp = 0
    last = 0
    now = 15
    action = ['l1', 'l0', 'f1', 'f0', 'd11', 'd10', 'd20', 'd21', 'w10',
              'w11', 'w20', 'w21', 'l1', 'l1', 'f1']
    action2 = ['f1', 'f0', 'd11', 'd10', 'd20', 'd21', 'w10',
              'w11', 'w20', 'w21']
    try:
        with open("dataset.txt", "a") as datafile:
            controlDoorTwo("0")
            controlDoorOne("0")
            controlWindowOne("0")
            controlWindowTwo("0")
            GPIO.output(lamp_pin, GPIO.LOW)
            GPIO.output(fanPin, GPIO.LOW)
            while True:
                now += 1
                choose = random.choice(action)
                if choose == 'l1' or choose == 'l0':
                    if now - last > 15:
                        last = now
                    else:
                        choose = random.choice(action2)
                print(choose)
                input = choose
                if roomA_temp > 90 or roomB_temp > 90:
                    input = 'l0'

                if input == "q" or input == "Q":
                    pass
                elif input[0] == "L" or input[0] == "l":
                    lamp_state = input[1]
                    controlLamp(input[1])
                elif input[0] == "F" or input[0] == "f":
                    fan_state = input[1]
                    controlFan(input[1])
                elif input[0:2] == "d1" or input[0:2] == "D1":
                    doorOne_state = input[2]
                    controlDoorOne(input[2])
                elif input[0:2] == "d2" or input[0:2] == "D2":
                    doorTwo_state = input[2]
                    controlDoorTwo(input[2])
                elif input[0:2] == "w1" or input[0:2] == "W1":
                    windowOne_state = input[2]
                    controlWindowOne(input[2])
                elif input[0:2] == "w2" or input[0:2] == "W2":
                    windowTwo_state = input[2]
                    controlWindowTwo(input[2])
                else:
                    controlDoorTwo("0")
                    controlDoorOne("0")
                    controlWindowOne("0")
                    controlWindowTwo("0")
                    GPIO.output(lamp_pin, GPIO.LOW)
                    GPIO.output(fanPin, GPIO.LOW)
                    GPIO.cleanup()

                aT, aH = getTemp(roomA_pin)
                bT, bH = getTemp(roomB_pin)
                cT, cH = getTemp(roomC_pin)
                dT, dH = getTemp(roomD_pin)
                oT, oH = getTemp(outside_pin)
                datafile.write(str(datetime.now()) + '\t')
                datafile.write(str(aT) +'\t')
                datafile.write(str(aH) + '\t')
                datafile.write(str(bT) +'\t')
                datafile.write(str(bH) + '\t')
                datafile.write(str(cT) +'\t')
                datafile.write(str(cH) + '\t')
                datafile.write(str(dT) +'\t')
                datafile.write(str(dH) + '\t')
                datafile.write(str(oT) +'\t')
                datafile.write(str(oH) + '\t')
                datafile.write(str(doorOne_state) + '\t')
                datafile.write(str(doorTwo_state) + '\t')
                datafile.write(str(windowOne_state) + '\t')
                datafile.write(str(windowTwo_state) + '\t')
                datafile.write(str(lamp_state) + '\t')
                datafile.write(str(fan_state) + '\n')
                time.sleep(5)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    except Exception as e: 
    	print(e)
    finally:
        GPIO.cleanup()

        
