#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import datetime
import requests

import influxdb_client
import os
from influxdb_client.client.write_api import SYNCHRONOUS


if os.getenv("FLASK_APP_ENABLED", False).lower() == "true":
    flask_app_enabled = True
    flask_app_url = os.getenv("FLASK_APP_URL")
if os.getenv("INFLUXDB_ENABLED", False).lower() == "true":
    influxdb_enabled = True
    token = os.environ.get("INFLUXDB_TOKEN")
    org = os.environ.get("INFLUXDB_ORG")
    url = os.environ.get("INFLUXDB_URL")
    bucket = os.environ.get("INFLUXDB_BUCKET")
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)

SENSOR_PIN = os.environ.get("SENSOR_PIN")
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

seconds = 0


def callback(channel):
    print(str(datetime.datetime.now()) + ' Impulse detected')
    if flask_app_enabled:
        flaskapp()
    if influxdb_enabled:
        influxdb()


def flaskapp():
    requests.post(flask_app_url, json={'power': 2})


def influxdb():
    point = (
        influxdb_client.Point("electricity")
        .field("consumption", 2)
    )
    write_api.write(bucket=bucket, org="finn", record=point)


influxdb()

try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=callback, bouncetime=500)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
GPIO.cleanup()
