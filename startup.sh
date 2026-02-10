#!/bin/bash
python manage.py migrate --noinput
./tailwindcss -i static/css/input.css -o static/css/style.css --minify
python manage.py collectstatic --noinput
gunicorn watjesblog.wsgi --bind=0.0.0.0:8000
