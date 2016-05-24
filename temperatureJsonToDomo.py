#!/usr/bin/python

#import library to do http requests:
import urllib2

#import the One-wire thermometer library
from w1thermsensor import W1ThermSensor

#define variables for Domoticz
domourl1 = 'http://X.X.X.X:8080/json.htm?type=command&param=udevice&idx='
domourl2 = '&nvalue=0&svalue='
tempid = 'XX'
temp2id = 'XX'

#This is the first sensor.
sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "XXXXXXXXX")
temperature1_in_celsius = sensor1.get_temperature()

print temperature1_in_celsius

sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "XXXXXXXXX")
temperature2_in_celsius = sensor2.get_temperature()

print temperature2_in_celsius

#  See link below of doc
#  https://www.domoticz.com/wiki/Domoticz_API/JSON_URL's#Temperature
#create URL and send to Domoticz
tempurl = domourl1 + tempid + domourl2 + str(temperature1_in_celsius)
urllib2.urlopen(tempurl)

#create URL and send to Domoticz
tempurl2 = domourl1 + temp2id + domourl2 + str(temperature2_in_celsius)
urllib2.urlopen(tempurl2)
