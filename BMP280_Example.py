from Adafruit_BME280 import *
import time

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

f = open('/root/Sensor_Data/Pressure/Pressure_Data.txt','a')
#
while True:
	degrees = sensor.read_temperature()
	pascals = sensor.read_pressure()
	hectopascals = pascals / 100


	print 'Temp      = {0:0.3f} deg C'.format(degrees)
	print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
        print (degrees, pascals)
	file = f
	print (file)

#pressure, temperature = sensor
#ead_retry(sensor, pin)
#data = degrees, pascals
#textdata = str(data)
#f.write(textdata+'\n')
	time.sleep(2.0)
