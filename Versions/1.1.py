import datetime ##import date and time, plus other stuff idk if we need
import time 
#import ntplib
import os
import sys

import smbus
import time

from Adafruit_BME280 import *


#SHT31-D
bus = smbus.SMBus(1) # Get I2C bus
    bus.write_i2c_block_data(0x44, 0x2C, [0x06])
	data = bus.read_i2c_block_data(0x44, 0x00, 6)

#BME280
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)


#i=0 #set i=0 for a start, or we could use true

while True: #while loop

    file = open("Untitled1.txt", "a") #open file in append mode
    rawstamp = time.time() #time stamp value
    dtstamp = datetime.datetime.fromtimestamp(rawstamp).strftime('%Y-%m-%d %H: %M: %S') # convert raw time stamp to date time format
    file.write("Time stamp: " +dtstamp+ '\n')#creating a time stamp
    
    #SHT31-D
    #Read outs
    temp = data[0] * 256 + data[1]
	cTemp = -45 + (175 * temp / 65535.0)
	fTemp = -49 + (315 * temp / 65535.0)
	humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
	
	#append to file
#	file.write(+ctemp+ '\n\')
	file.write(+ftemp+ '\n')
	file.write(+humidity+ '\n')'
	time.sleep(2.0) #2 second timer 
	
	#BME280
	degrees = sensor.read_temperature()
	pascals = sensor.read_pressure()
	hectopascals = pascals / 100
    
    #append to file
    file.write(+pascals+ '\n')
	time.sleep(2.) #2 second timer
	
#print "end of loop" #not really necessary 
file = open("Untitled1.txt", "r") #have to open file again in read mode 
print file.readlines() #read out 

file.close(