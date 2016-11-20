# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.9.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise

## How to Use

To use this project, follow these steps:

1. Create your working environment inside a dir with `$ python3 -m venv env`
2. Activate Virtual Env with `$ source env/bin/activate`
3. Install Django (`$ pip install django`)
4. Create a new project using this template
5. `$ pip install -r dev-requirements.txt`
6. `$ mv helloworld/settings{.rename.ini,.ini}`

## Creating Your Project

Using this template to create a new Django app is easy:

    $ django-admin startproject --template=https://github.com/Leeaandrob/django-template-products/archive/master.zip --extension=ini,py --name=Procfile helloworld .

You can replace ``helloworld`` with your desired project name.

## First deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create {{ project_name }}
    $ heroku config:set SECRET_KEY='{{ secret_key }}'
    $ heroku config:set MANO_APPLICATION_NAME={{ project_name }}
    $ heroku config:set MANO_URL=https://accounts.mano.cx/
    $ heroku config:set DEBUG=False
    $ heroku config:set FORCE_SSL=False
    $ heroku config:set RAVEN_URL={{ SENTRY DSN URL }}
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
