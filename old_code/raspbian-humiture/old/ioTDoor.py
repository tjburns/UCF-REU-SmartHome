#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
sender="linearhallsensor@gmail.com"
passw="ucfhec315"
subject="Someone entered the room"
mesg="I wanted you to know"

digital= 15
flag=True

print "Close the door before writing email address" 

recvr=raw_input("Enter receiver address: ")
msg['From'] = sender
msg['To'] = recvr
msg['Subject'] = subject
message = mesg
msg.attach(MIMEText(message))

server = smtplib.SMTP('smtp.gmail.com', 587)
#server.ehlo()
server.starttls()
#server.ehlo()
server.login(sender,passw)
	
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
			server.sendmail(sender, recvr, msg.as_string())
			flag=False
		time.sleep(0.5)



if __name__ == '__main__':
        setup()
        
	

        try:
    # Loop until users quits with CTRL-C
		signal1=GPIO.input(digital) 
                if signal1 == 0:
			print "Close the door first before running"
		else:
			loop()

        except KeyboardInterrupt:
    # Reset GPIO settings
                GPIO.cleanup()
