#! /bin/sh

source venv/bin/activate
gunicorn ourwork_wagtail.wsgi:application --bind 0.0.0.0:8000 --workers 3

