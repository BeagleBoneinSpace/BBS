import datetime ##import date and time, plus other stuff idk if we need
import time 
import os
import sys
import smbus
import time

from Adafruit_BME280 import *

#BME280
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

while True: #while loop

    file = open("/home/debian/Desktop/Sensor_File_Transfers/BMP280.txt", "a") #open file in append mode
    rawstamp = time.time() #time stamp value
    dtstamp = datetime.datetime.fromtimestamp(rawstamp).strftime('%Y-%m-%d %H: %M: %S') # convert raw time stamp to date time format
    file.write("Time stamp: " +dtstamp+ '\n')#creating a time stamp

	#BME280
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    
    
    print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)

    #append to file
    #file.write(+pascals+ '\n')
    file.write(str(round(hectopascals,2)))
    file.write(" kPa\n")
    file.write("\n")


    time.sleep(2.) #2 second timer
	
#print "end of loop" #not really necessary 
file = open("/home/debian/Desktop/Sensor_File_Transfers/BMP280.txt", "r") #have to open file again in read mode 
print file.readlines() #read out 

file.close()