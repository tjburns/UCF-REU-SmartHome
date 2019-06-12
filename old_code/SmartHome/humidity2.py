import Adafruit_DHT
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=16
gpio2=12

file = open("templog.txt", "w")

while True:
    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    h2, t2 = Adafruit_DHT.read_retry(sensor, gpio2)
     
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity > 100:
        file.write("Bad data\t")
    elif humidity is not None and temperature is not None:
        temp = (temperature * 9.0 / 5.0) + 32
        file.write('Temp={0:0.2f}*F  Humidity={1:0.2f}%\t'.format(temp, humidity))
    else:
        file.write('Failed to get reading. Try again!\t')


    if h2 > 100:
        file.write("Bad data\n")
    elif h2 is not None and t2 is not None:
        temp2 = (t2 * 9.0 / 5.0) + 32
        file.write('Temp={0:0.2f}*F  Humidity={1:0.2f}%\n'.format(temp2, h2))
    else:
        file.write('Failed to get reading. Try again!\n')
