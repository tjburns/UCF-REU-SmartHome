import Adafruit_DHT
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=6
 
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
if humidity > 100:
    print("Bad data")
elif humidity is not None and temperature is not None:
    temp = (temperature * 9.0 / 5.0) + 32
    print('Temp={0:0.2f}*F  Humidity={1:0.2f}%'.format(temp, humidity))
else:
    print('Failed to get reading. Try again!')
