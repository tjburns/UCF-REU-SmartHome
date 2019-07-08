import RPi.GPIO as GPIO
import time
import os
import random

from pin_control import *

def sequence_random():
	#TODO easiest sequence
		#randomize events
	
	num_ops = random.randint(1,6)
	for _ in range(num_ops):
            random_motor = random.randint(0,15)
            if motor_states[random_motor] == 'closed':
                motorOpen(random_motor)
                motor_states[random_motor] = 'open'
                print(motor_names[random_motor] + ' opened')
            elif motor_states[random_motor] == 'open':
                motorClose(random_motor)
                motor_states[random_motor] = 'closed'
                print(motor_names[random_motor] + ' closed')

#def sequence_NormalDay():
	#TODO write method simulating a normal day:
		# wake up
		# make breakfast
		# shower, etc
		# leave for half the day
		# come home - relax/go to bathroom/cook dinner
