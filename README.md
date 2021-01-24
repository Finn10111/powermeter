# powermeter

Simple Flask based application to receive impulses via cURL from a power meter.

Clone this repository and create a virtualenv within it:

```
git clone https://github.com/Finn10111/powermeter.git
cd powermeter
virtualenv -p /usr/bin/python3 .
# or if python3 is your default:
virtualenv .
pip install -r requirements.txt
```

For developing run this (you need to create database and user first):

```
export FLASK_ENV=development
export APP_DEVELOPMENT_DATABASE_URI=postgres://username:passwort@hostname/database
flask run
```
