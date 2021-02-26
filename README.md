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

```sh
$ curl -LX GET http://127.0.0.1:8000/api/quiz/ -H 'Authorization: Token 1403663acd1f84929d10fe98ca69ca88e83de84d'
```

## Get/Add/Change/Delete Quiz

```
Get: api/quiz/ return {
    "id": 11,
    "question": [
        7
    ],
    "name": "О себе",
    "date_start": "2021-02-26T15:02:57.664934Z",
    "date_finish": null,
    "desc": "Опрос о себе"
}

Add: api/quiz/create with data - name, desc, return serialized new obj

Change: api/quiz/update/<int:pk>/ with data - name, desc, return serialized update obj

Delete: api/quiz/delete/<int:pk>/ return 204
```


## Get/Add/Change/Delete Question

```
Get: api/question/ return {
    "text": "\"Ваши качества?\"",
    "type": "ManyQ",
    "quiz": 11,
    "choice_answer": [
        26,
        27,
        28
    ],
    "answer": [
        7,
        8
    ]
}

Add: api/question/create with data - quiz, text, type, answers(optional, sep ",") return serialized create obj

Change: api/question/update/<int:pk>/ with data - quiz, text, type, answers(optional, sep ",") return serialized update obj

Delete: api/question/delete/<int:pk>/ return 204
```

## Get user Quiz

```
get request answer/get/<int:id>/ return {
    "answers": [
        {
            "id": 7,
            "choice": "Норм",
            "text": null,
            "question": 7,
            "user": [
                1
            ]
        },
        {
            "id": 8,
            "choice": " нет",
            "text": null,
            "question": 7,
            "user": [
                1
            ]
        },
        {
            "id": 9,
            "choice": " нет",
            "text": null,
            "question": 7,
            "user": [
                1
            ]
        }
    ],
    "quiz": [
        {
            "id": 11,
            "question": [
                7
            ],
            "name": "О себе",
            "date_start": "2021-02-26T15:02:57.664934Z",
            "desc": "Опрос о себе"
        }
    ]
}
```

## Create answer

```
post reauest answer/create/ return {
    "id": 9,
    "text": null,
    "question": 7,
    "choice": 27,
    "user": [
        1
    ]
}
```
