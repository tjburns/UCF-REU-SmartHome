import RPi.GPIO as GPIO
import time
from datetime import datetime
import os
import Adafruit_DHT
from adafruit_servokit import ServoKit

from pin_control import *
from sequences import *


 # PWM 0 - 6 : doors
 # PWM 8 - 15 : windows
 # 00 : Bedroom 2 - Bathroom
 # 01 : Bedroom 1 - Living Rm
 # 02 : Living Rm - Kitchen
 # 03 : Living Rm - Bathroom
 # 04 : Bedroom 1 - Bathroom
 # 05 : Living Rm - Front Door
 # 06 : Bedroom 1 - Back Door
 #----------------------------
 # 08 : Bedroom 1, 2 ft.
 # 09 : Living Rm, 2 ft.
 # 10 : Bedroom 2, 2 ft
 # 11 : Kitchen, 2 ft.
 # 12 : Bedroom 2, 3 ft.
 # 13 : Living Rm, 3 ft.
 # 14 : Kitchen, 3 ft.
 # 15 : Bedroom 1, 3 ft.
def debug_loop():
    try:
        while True:
            print('Enter desired operation')
            op = input().lower()
            words = op.split()
            if op == 'open all':
                print("opening all doors and windows")
                openAll()
            elif op == 'close all':
                print("closing all doors and windows")
                closeAll()
            elif op == 'open all doors':
                print("opening all doors")
                openAllDoors()
            elif op == 'close all doors':
                print("closing all doors")
                closeAllDoors()
            elif op == 'open all windows':
                print("opening all windows")
                openAllWindows()
            elif op == 'close all windows':
                print("closing all windows")
                closeAllWindows()
            elif words[0] == 'open':
                #open based on pin number
                print("opening " + motor_names[int(words[1])])
                motorOpen(int(words[1]))
            elif words[0] == 'close':
                #close based on pin number
                print("closing " + motor_names[int(words[1])])
                motorClose(int(words[1]))
            else:
                print('Incorrect input.')
    
    except KeyboardInterrupt:
        print("Keyboard interrupt.")
    except Exception as e: 
        print(e)

if __name__ == '__main__':
    
    closeAll()
    
    # perform desired scenario for data collection -- basically just the runner file with the debug loop method if necessary
    
    #SEQUENCE_aNormalDay()
    
    demo()
