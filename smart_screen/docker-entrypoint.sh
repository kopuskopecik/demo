#!/bin/bash
# python3 /smart_screen/manage.py makemigrations
# python3 /smart_screen/manage.py migrate
pypy3 /smart_screen/manage.py runserver 0.0.0.0:8000
#gunicorn smart_screen.wsgi:application --bind 0.0.0.0:8000  --worker-class gevent --worker-connections 1000 --workers 8 --timeout 30 --keep-alive 32  --error-logfile gunicorn_error.log  --log-level info