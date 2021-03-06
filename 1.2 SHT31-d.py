import datetime ##import date and time, plus other stuff idk if we need
import time 
import os
import sys
import smbus
import time

#SHT31-D
bus = smbus.SMBus(1) # Get I2C bus

while True: #while loop

    bus.write_i2c_block_data(0x44, 0x2C, [0x06])
    data = bus.read_i2c_block_data(0x44, 0x00, 6)

    file = open("/home/debian/Desktop/Sensor_File_Transfers/SHT31-D.txt", "a") #open file in append mode
    rawstamp = time.time() #time stamp value
    dtstamp = datetime.datetime.fromtimestamp(rawstamp).strftime('%Y-%m-%d %H: %M: %S') # convert raw time stamp to date time format
    file.write("Time stamp: " +dtstamp+ '\n')#creating a time stamp
    
    #SHT31-D
    #Read outs
    temp = data[0] * 256 + data[1]
    cTemp = -45 + (175 * temp / 65535.0)
    fTemp = -49 + (315 * temp / 65535.0)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
    ftemp = str(fTemp)
    
    #humidity = str(humidity)
	
	#append to file

    file.write(str(round(fTemp,2)))
    file.write(" F \n")
    file.write(str(round(humidity,2)))
    file.write(" % RH \n")
    print "Temperature in Fahrenheit is : %.2f F" %fTemp
    #print "Temperature in Celsius is : %.2f C" %cTemp
    print "Relative humidity  is : %.2f %%RH" %humidity
    time.sleep(2.0) #2 second timer 
	

    #print "end of loop" #not really necessary 
    file = open("/home/debian/Desktop/Sensor_File_Transfers/SHT31-D.txt", "r") #have to open file again in read mode 
    #print file.readlines() #read out 

file.close()
