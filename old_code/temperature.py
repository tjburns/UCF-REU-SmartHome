#!/usr/bin/env python
#
# Analog Input with ADC0832 chip
#
# Datasheet: http://www.ti.com/lit/ds/symlink/adc0838-n.pdf
# Part of SunFounder LCD StarterKit
# http://www.sunfounder.com/index.php?c=show&id=21&model=LCD%20Starter%20Kit
#

import time
import os
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
PIN_CLK = 18
PIN_DO  = 27
PIN_DI  = 26
PIN_CS  = 17

# set up the SPI interface pins
GPIO.setup(PIN_DI,  GPIO.OUT)
GPIO.setup(PIN_DO,  GPIO.IN)
GPIO.setup(PIN_CLK, GPIO.OUT)
GPIO.setup(PIN_CS,  GPIO.OUT)

# read SPI data from ADC8032
def getADC(channel):
	# 1. CS LOW.
        GPIO.output(PIN_CS, True)      # clear last transmission
        GPIO.output(PIN_CS, False)     # bring CS low

	# 2. Start clock
        GPIO.output(PIN_CLK, False)  # start clock low

	# 3. Input MUX address
        for i in [1,1,channel]: # start bit + mux assignment
                 if (i == 1):
                         GPIO.output(PIN_DI, True)
                 else:
                         GPIO.output(PIN_DI, False)

                 GPIO.output(PIN_CLK, True)
                 GPIO.output(PIN_CLK, False)

        # 4. read 8 ADC bits
        ad = 0
        for i in range(8):
                GPIO.output(PIN_CLK, True)
                GPIO.output(PIN_CLK, False)
                ad <<= 1 # shift bit
                if (GPIO.input(PIN_DO)):
                        ad |= 0x1 # set first bit

        # 5. reset
        GPIO.output(PIN_CS, True)

        return ad

if __name__ == "__main__":
    tolerance = 0.2 # degrees
    value = 1.0*(getADC(1))
    print(value)
    # calibrate the formula with a termometer
    lasttemp = value *0.5# formula made through Wolfram Alpha: 'linear function (0,125);(720,0);(1023,-55)', where (readvalue, temperature)
    print('Temperature: %5.2f' % lasttemp)
    while True:
            value = getADC(1)
            #digital = GPIO.input(digitalPin)
            #temp = 3.3 * value
	    #temp /= 1024
	    #temp = (temp - 0.1) * 100
	    temp = 25.4+(0.3*value)
	    #temp = (temp * 9.0 / 5.0) + 32.0;
            if ((temp > lasttemp + tolerance) or (temp < lasttemp - tolerance)): # if temperature changed more than the tolerance
                    print('New temperature: %5.2fC (input: a: %3d,)' % (temp, value))
                    lasttemp = temp
            time.sleep(2)

            
    #while True:
     #       if(getADC(1)==128):
      #          print "ADC[0]: {}\t ADC[1]: {}".format(getADC(0), getADC(1))
       #         Vr = 5 * float(getADC(0)) / 255                
	#	Rt = 10000 * Vr / (5 - Vr)
	#	temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
	#	temp = temp - 273.15
	#	print 'temperature = %d C' % temp
         #       time.sleep(1)
