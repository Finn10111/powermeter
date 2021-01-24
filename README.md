# powermeter

Simple Flask based application to receive impulses via cURL from a power meter.

For developing run this (you need to create database and user first):

```
export FLASK_ENV=development
export APP_DEVELOPMENT_DATABASE_URI=postgres://username:passwort@hostname/database
flask run
```
