import RPi.GPIO as GPIO
import time
import os
import random

def sequence_random():
	#TODO easiest sequence
		#randomize events
	
	try:
		while True:
			num_ops = random.randint(1,6)
			for _ in range(num_ops):
				random_motor = random.randint(0,16)
				if state[random_motor] == 'closed':
					motorOpen(random_motor)
					state[random_motor] = 'open'
					print(motor_names[random_motor] + ' opened')
				elif state[random_motor] == 'open':
					motorClose(random_motor)
					state[random_motor] = 'closed'
					print(motor_names[random_motor] + ' closed')
					
			for i in range(0,300):
				print('Next action in: ' + str(i)+'/300', flush=True)
				time.sleep(1)
	except KeyboardInterrupt:
		print("Keyboard interrupt.")
	except Exception as e: 
		print(e)

def sequence_NormalDay():
	#TODO write method simulating a normal day:
		# wake up
		# make breakfast
		# shower, etc
		# leave for half the day
		# come home - relax/go to bathroom/cook dinner
