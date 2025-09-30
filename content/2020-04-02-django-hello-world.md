---
layout: post
lang: en
title: Django Hello World
slug: django-hello-world
author: Martin Thoma
status: draft
date: 2019-01-17 20:00
category: My bits and bytes
tags: Machine Learning
featured_image: logos/star.png
---
In the development of a bigger web service you have several key components:

* Views: Display single things (`views.py`)
* Routing: Map URLs to views (`urls.py`)

<table class="table">
    <tr>
        <th>Standard</th>
        <th>Django</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Model</td>
        <td>Model</td>
        <td>application's dynamic data structure; receives input from controller</td>
    </tr>
    <tr>
        <td>View</td>
        <td>Template</td>
        <td>How the content gets presented to the user</td>
    </tr>
    <tr>
        <td>Controller</td>
        <td>View</td>
        <td>data that gets presented to the user (content)</td>
    </tr>
</table>


## Project and App

Create a project:

```text
$ django-admin startproject mysite
$ tree mysite
mysite
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Create an app:

```shell
$ cd mysite
$ python manage.py startapp polls
$ tree .
.
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

```

Create DB:

```shell
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Make migrations - files that tell Django that the model changed and how it
changed:

```shell
$ python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Choice
    - Create model Question
    - Add field question to choice
```


## Views

Content is delivered by views. A simple view looks like this:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

## ORM

```shell
$ python manage.py shell
In [2]: Question.objects.all()
Out[2]: <QuerySet [<Question: What's new?>]
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>
```


## Other commands

Interactive shell

```shell
$ python manage.py shell
```

Create an admin (superuser):

```shell
$ python manage.py createsuperuser
```

## See also

* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
