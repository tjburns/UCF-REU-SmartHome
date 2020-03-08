import RPi.GPIO as GPIO
import time
import os
import random

from pin_control import *

def set_state_named_motor(motor, state):

    current_state = motor_states_pinRef[motor]

    if state == current_state:
        print("this motor is already %s" % current_state)
    else:
        if state == 'open':
            motorOpen(motor_names_pinRef[motor])
            motor_states_pinRef[motor] = 'open'
            print("%s : open" % motor)
        elif state == 'closed':
            motorClose(motor_names_pinRef[motor])
            motor_states_pinRef[motor] = 'closed'
            print("%s : closed" % motor)