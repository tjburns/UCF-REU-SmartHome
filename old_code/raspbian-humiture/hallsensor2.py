#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

digital= 15
flag=True
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("linearhallsensor@gmail.com", "ucfhec315")
msg = "Alarm Message"

	
def setup():
        GPIO.setwarnings(False) 
	GPIO.setmode(GPIO.BOARD)
        GPIO.setup(digital,GPIO.IN)
        
        
def loop():
	while True:
		signal1=GPIO.input(digital) 

		if signal1 == 1:
			flag = True
		elif flag:
			server.sendmail("linearhallsensor@gmail.com", "4077576496@txt.att.net", msg)
			flag=False
		time.sleep(0.5)



if __name__ == '__main__':
        setup()
        
	

        try:
    # Loop until users quits with CTRL-C
                loop()

        except KeyboardInterrupt:
    # Reset GPIO settings
                GPIO.cleanup()
