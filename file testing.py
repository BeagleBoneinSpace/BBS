import datetime ##import date and time, plus other stuff idk if we need
import time 
#import ntplib
import os
import sys

i=0 #set i=0 for a start, or we could use true

while (i<9): #while loop

    file = open("Untitled1.txt", "a") #open the file in append mode, maybe swap to r+? might not work for keeping old data

    #from datetime import datetime
    rawstamp = time.time() #time stamp value
    dtstamp = datetime.datetime.fromtimestamp(rawstamp).strftime('%Y-%m-%d %H: %M: %S') # convert raw time stamp to date time format

    file.write("Time stamp: " +dtstamp+ '\n')#creating a time stamp, we can edit all this to fit code
    file.write("Hello 1234 \n")
    
    i=i+1 #incriment 
    
    file = open("Untitled1.txt", "r") #have to open file again in read mode 
    print file.readlines() #read out 
    
    
print "end of loop" #not really necessary 
file = open("Untitled1.txt", "r") #have to open file again in read mode 
print file.readlines() #read out 

file.close()