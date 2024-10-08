# whenever we start to run the application, we migrate the db
#! /bin/bash

sleep 10
python3 manage.py makemigrations
python3 manage.py migrate