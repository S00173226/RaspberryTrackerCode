#!/usr/bin/python3

import requests
from datetime import datetime as dt
import gpsd
import RPi.GPIO as GPIO
from pirc522 import RFID
import os
from time import sleep

rdr = RFID()
latitude = 0.0
longtitude = 0.0



exists = os.path.isfile('/home/pi/')
try:

            rdr.wait_for_tag()
 
            

            
finally:
        GPIO.cleanup()

while True:
    try:
        gotData = 0
        gpsd.connect()
        packet = gpsd.get_current()
        position = packet.position()
            
        latitude = position[0]
        longtitude = position[1]
        today_date = dt.today().strftime('%Y-%m-%d %H:%M:%S')
        url = "http://ec2-52-19-66-117.eu-west-1.compute.amazonaws.com:3000"
        payload = {
            'Device_ID': 2,
            'User_ID': 1,
            'Date_Time_Recorded': today_date,
            'Latitude': latitude,
            'Longitude': longtitude
        }
        print(payload)
        r = requests.post(url, json=payload)
        print(r.status_code)
        print(r.text)
    
    except(KeyboardInterrupt, SystemExit):
        print("Exiting")
    except:
        print("Unexpected error:", sys.exec_info()[0])

time.sleep(1200 - time.time() % 1200)



