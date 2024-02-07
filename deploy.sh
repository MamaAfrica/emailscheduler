#!/bin/bash
#Create a virtual environment
python3 -m venv venv
#Activate the virtual environment
source venv/bin/activate

#Install dependencies from requirements.txt
pip install -r requirements.txt

#Run database migrations
python manage.py migrate

#Collect static files
python manage.py collectstatic --noinput

#Run the Django application
python manage.py runserver 0.0.0.0:8000

sudo supervisorctl start emailbotapp