# powermeter


A simple Pyhton script to mesaure you electricity consumption using the LED on a electricity meter and a digital light sensor.

You either can use InfluxDB to store the data or a built in Flask application.

## Hardware setup

- Raspberry Pi
- Digital light sensor like this: https://www.berrybase.de/lichtsensor-mit-digitalem-ausgang

Connect the light sensor to your Pi:

```
VCC: 5V
DATA: GPIO 27
GND: GND
```

## Software setup

- Copy the `.env.example` to `.env` and change it to your needs.
- Acivate at least InfluxDB (which I would recommend) or Flask output.

Clone this repository and create a virtualenv within it:

```
git clone https://code.f2n.me/finn/powermeter.git
cd powermeter
virtualenv .
pip install -r requirements.txt
```

## Developing (Flask app)

For developing run this (you need to create database and user first):

```
export FLASK_ENV=development
export APP_DEVELOPMENT_DATABASE_URI=postgres://username:passwort@hostname/database
flask run
```

## Screenshots

Node-RED usage example:

![Node-RED Dashboard](/screenshots/nodered.png)

Grafana Dashboard example (InfluxDB datasource):

![Grafana Dashboard](/screenshots/grafana.png)





