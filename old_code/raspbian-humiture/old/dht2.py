from subprocess import Popen, PIPE
#import subprocess

for line in Popen(['sudo','./rajarshi'], stdout=PIPE):
    print line  
