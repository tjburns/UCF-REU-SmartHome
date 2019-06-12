#!/bin/bash
for f in config*.txt
do	
for number in {1..200}
do
java -jar UAON.jar $f
done
mv Report report$f
done
