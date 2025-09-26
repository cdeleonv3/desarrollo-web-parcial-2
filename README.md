# Parcial 1
## Configuaracion inicial
`python3 -m venv venv`
`python -m pip install --upgrade pip setuptools wheel`
`pip install django`
`django-admin startproject config .`
`django manage.py startapp core`
## Migracion
`python manage.py makemigrations`
`python manage.py migrate`
