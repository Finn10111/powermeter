#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import datetime
import requests
 
SENSOR_PIN = 27
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
seconds = 0

def callback(channel):
    print(str(datetime.datetime.now()) + ' Impulse detected')
    url = 'http://powermeter.local/impulses'
    requests.post(url, json = {'power': 2})

try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=callback, bouncetime=500)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
GPIO.cleanup()
