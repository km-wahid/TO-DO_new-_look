# Django To-Do Web Application

A simple web application to manage your to-do tasks built with Django.

## Features

- User authentication (login and registration)
- Create, update, delete, and view tasks
- Mark tasks as complete
- Search tasks
- Reorder tasks

## Prerequisites

- Python 3.x
- Django 3.x or later

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/django-todo-app.git
   cd django-todo-app
## Create virtual enviornment 
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

## Apply migration
python manage.py migrate

## Create superuser
python manage.py createsuperuser

## Run the Development sever
python manage.py runserver

## Visit the web
http://127.0.0.1:8000


# Requiments

Django>=3.0,<4.0 
djangorestframework
django-crispy-forms
psycopg2-binary
gunicorn
whitenoise
