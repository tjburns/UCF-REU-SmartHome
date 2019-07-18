import RPi.GPIO as GPIO
import time
import os
import random

from pin_control import *

MOTOR_STATE_FILE = "motor_states_NormalDay.txt"

def write_motor_states():
	with open(MOTOR_STATE_FILE, "a") as motors:
       		motors.write(str(datetime.now()) + '\t')
       	
       		print()
			for i in motor_states:
				print(motor_states[i] + '\t', end = '')
				motors.write(motor_states[i] + '\t')
                
			print()
           	motors.write('\n')

def HELPER_random_choose_motors():

	num_ops = random.randint(1,15)
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

def SEQUENCE_random():
	closeAll()
    while True:
    
   		HELPER_random_choose_motors()
        
        write_motor_states()
            
       	print()
		for i in range(0,300):
			print('Next action in: ' + str(i)+'/300', flush=True)
			time.sleep(1)
                
def SEQUENCE_NormalDay():
	#TODO write method simulating a normal day:
	# - since 2 bedroom home imagine a couple with one child
	
	#	family wakes up - sun down for one hour
	#	parent1: bathroom -> shower/change -> join breakfast -> leave(bedroom1->bathroom->kitchen->bathroom->front door)
	#	parent2: make breakfast -> bathroom -> shower/change -> leave(bedroom1->livingroom->kitchen->bathroom->front door)
	#	child: shower -> change -> join breakfast -> leave(bedroom2->bathroom->bedroom2->kitchen->front door)
		
	#	inital thoughts
	#		LMAO this would actually be best done with threads xd
	#		so uh i'm not gonna do that cuz uh yeah -- 'future work' hehe have fun
	#		(also i don't know how to do threading in python)
	
	# yeah so i wrote a bit then decided i'm not gonna do that and i'm going to just listen to Safa's recomendation and just do a couple short sequences
	# but i'll start with the morning scenario i described above
	
	
def SEQUENCE_avgMorning():
	# this sequence will be recording data every second and last for about an hour
	# -- will provide ~the same number of data points as our random dataset for a full day's recording
	
	motorOpen(4)
	motorOpen(1)
	time.sleep(2)
	motorClose(4)
	motorClose(1)
	
	motorOpen(2)
	time.sleep(2)
	motorClose(2)
	
	# parent 1 showering, parent 2 making breakfast
	time.sleep(300)
	
	motorOpen(3)
	time.sleep(2)
	motorClose(3)
	
	motorOpen(2)
	time.sleep(2)
	motorClose(2)
	
	motorOpen(0)
	time.sleep(2)
	motorClose(0)
	time.sleep(300)
	motorOpen(0)
	time.sleep(2)
	motorClose(0)
	motorOpen(3)
	time.sleep(2)
	motorClose(3)
	
	motorOpen(3)
	time.sleep(2)
	motorClose(3)
	time.sleep(300)
	motorOpen(4)
	time.sleep(2)
	motorClose(4)
	time.sleep(120)
	motorOpen(1)
	time.sleep(2)
	motorClose(1)
	
	motorOpen(5)
	time.sleep(2)
	motorClose(5)
