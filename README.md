# TestWork QuizApi

This is an test work QuizApi

**This example is written with Django 3.1.7. Unless you specifically
need an new Django version you should contact me as a separate order **

Running this app on your local machine in development will work as
well, although i don't sure)


## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ pip install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000/api/quiz/` to view the app. Alternatively you
can use postman.):


## Authorization


```sh
$ curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'username=kk23&password=123123123'
{"auth_token":"1403663acd1f84929d10fe98ca69ca88e83de84d"}
```
