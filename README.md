# Curinculim Vite App

This application tries to facilitate the version control of your CV and cover letter per each application. This application is created on django and it’s meant to be run locally to protect your privacy. In future realices will be fully integrated with open AI API to help with writing.

## Stack:
- Django
- HTMX

## This application is 50% done.


## Installation:

```bash
python -m venv venv
source venv/bin/activate
python manage.py migrate
python manage.py runserver

```

Celery configuration
```bash
docker run -d -p 6379:6379 redis
celery -A config worker -l INFO
```

## Refences:
- https://community.openai.com/t/different-output-when-using-n-for-linebreaks/271510/2
