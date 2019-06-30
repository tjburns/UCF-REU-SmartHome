"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

def closeMotor(pin):
    kit.servo[pin].angle = 60
def openMotor(pin):
    kit.servo[pin].angle = 180

while(True):
    openMotor(0)
    openMotor(1)
    openMotor(2)
    openMotor(3)
    openMotor(4)
    openMotor(5)
    
    openMotor(8)
    openMotor(9)
    openMotor(10)
    openMotor(11)
    openMotor(12)
    openMotor(13)
    openMotor(14)
    
    time.sleep(5)
    
    closeMotor(0)
    closeMotor(1)
    closeMotor(2)
    closeMotor(3)
    closeMotor(4)
    closeMotor(5)
    
    closeMotor(8)
    closeMotor(9)
    closeMotor(10)
    closeMotor(11)
    closeMotor(12)
    closeMotor(13)
    closeMotor(14)
    
    time.sleep(5)
"""
closeMotor(4)
openMotor(4)
time.sleep(5)
closeMotor(4)
"""