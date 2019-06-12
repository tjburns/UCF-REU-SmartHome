import ctypes
_sum = ctypes.CDLL('libsum.so')
_sum.our_function.argtypes = (ctypes.c_int,ctypes.c_int)
import wiringpi

# import os
# os.system("export LD_LIBRARY_PATH=/home/pi/Desktop")

def our_function():
    global _sum
    hum = _sum.our_function(ctypes.c_int(0), ctypes.c_int(0))
    temp = _sum.our_function(ctypes.c_int(1), ctypes.c_int(0))
    return float(hum),float(temp)

wiringpi.wiringPiSetup()
while True:
	hum,temp=our_function()
	print 'Python: Humidity= ',hum, 'Temp= ',temp
