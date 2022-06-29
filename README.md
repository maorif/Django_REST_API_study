# Django REST API with Django Rest Framework study 
Tutorial that I followed: https://youtu.be/c708Nf0cHrs

## steps to setup (I like using a virtual enviroment with pipenv):

Installing libraries:

```shell
pip install pipenv
pipenv shell
pipenv install -r requirements.txt
```

Creating a django superuser (only need to set username and password)

```shell
python backend/manage.py createsuperuser
```

Initializing django server

```shell
python backend/manage.py migrate
python backend/manage.py runserver 8000
```

You can open http://127.0.0.1:8000/admin/ and login with superuser


