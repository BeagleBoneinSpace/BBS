import datetime ##import date and time, plus other stuff idk if we need
import time 
import os
import sys
import smbus
import time

from Adafruit_BME280 import *


while True: #while loop

    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    file = open("Untitled1.txt", "a") #open file in append mode
    rawstamp = time.time() #time stamp value
    dtstamp = datetime.datetime.fromtimestamp(rawstamp).strftime('%Y-%m-%d %H: %M: %S') # convert raw time stamp to date time format
    file.write("Time stamp: " +dtstamp+ '\n')#creating a time stamp

	#BME280
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    
    deg = str(degrees)
    pas = str(pascals)
    
    #append to file
    file.write(str(deg))
    file.write("\n")
    file.write(str(pas))
    file.write("\n")
    #file.write(str(hectopascals))
    
    print 'Temp      = {0:0.3f} deg C'.format(degrees)
    print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
    print (degrees, pascals)
        
        
    time.sleep(2.) #2 second timer
	
#print "end of loop" #not really necessary 
file = open("Untitled1.txt", "r") #have to open file again in read mode 
print file.readlines() #read out 

file.close()