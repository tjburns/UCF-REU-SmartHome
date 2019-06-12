import subprocess
import urllib
import time

time.sleep( 10 )
while True:
	#x=subprocess.Popen(["sudo","/home/pi/Desktop/humiture"],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        x=subprocess.Popen(['sudo','./dht19'], stdout=subprocess.PIPE)
	output,err=x.communicate()
        #print output
        
	l1=output.split(',')
	#print l1
	l2=[float(x) for x in l1]
	humidity=l2[0]
	temperature=l2[1]
	fahrenheit=l2[2]
	if humidity > 100 or temperature == 1000 or temperature < 0:
		continue
	# print l2
	print 
	print " Humidity = ", humidity," Temperature= ", fahrenheit, " [Time = ", time.asctime(time.localtime(time.time())), "]"
	
	url = "http://safa.x10host.com/iot/Weather/add.php?t="+str(fahrenheit)+"&h="+str(humidity)
	f = urllib.urlopen(url)
	time.sleep(30)
