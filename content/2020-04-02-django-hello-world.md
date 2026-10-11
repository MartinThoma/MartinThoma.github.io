---
layout: post
title: Django Hello World
slug: django-hello-world
lang: en
author: Martin Thoma
date: 2019-01-17 20:00
category: My bits and bytes
tags: Python, Django, Web Development
featured_image: logos/star.png
status: draft
---
In the development of a bigger web service, you have several key components:

* Models: The data and how it is stored (`models.py`)
* Views: Display single things (`views.py`)
* Routing: Map URLs to views (`urls.py`)
* Templates: The HTML that gets filled with the data (`templates/`)

Django names these parts a bit differently than the classic
model–view–controller pattern:

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

This article is a compact version of the first parts of the
[official tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/):
a small poll application.


## Project and App

Install Django:

```text
$ pip install django
```

Create a project:

```text
$ django-admin startproject mysite
$ tree mysite
mysite
├── manage.py
└── mysite
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

A *project* is the whole website with its settings. An *app* is one part of it
with its own models, views and templates; a project can have many apps, and an
app can be reused in other projects.

Create an app:

```shell
$ cd mysite
$ python manage.py startapp polls
$ tree .
.
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

```

Register the app in `mysite/settings.py`:

```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
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

By default, Django uses an SQLite database in the file `db.sqlite3`; the
`DATABASES` setting switches to PostgreSQL or MySQL.


## Models

Models are Python classes; Django creates the tables from them. In
`polls/models.py`:

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

Make migrations - files that tell Django that the model changed and how it
changed:

```shell
$ python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

`python manage.py migrate` applies them to the database. Commit the migration
files: every developer and every server runs the same migrations.


## Views

Content is delivered by views. A simple view looks like this:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

## Routing

The app gets its own `polls/urls.py`:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

and the project includes it in `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

Start the development server and open
`http://127.0.0.1:8000/polls/` in the browser:

```shell
$ python manage.py runserver
```


## Templates

Real pages are not built with string concatenation. Put the HTML into
`polls/templates/polls/index.html`:

```html
<h1>Latest questions</h1>
<ul>
{% for question in latest_question_list %}
    <li>{{ question.question_text }}</li>
{% empty %}
    <li>No polls are available.</li>
{% endfor %}
</ul>
```

and render it from the view:

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(
        request, "polls/index.html", {"latest_question_list": latest_question_list}
    )
```


## ORM

The models give you a query API, no SQL needed
([docs](https://docs.djangoproject.com/en/stable/topics/db/queries/)):

```text
$ python manage.py shell
>>> from django.utils import timezone
>>> from polls.models import Question
>>> q = Question.objects.create(question_text="What's new?", pub_date=timezone.now())
>>> Question.objects.all()
<QuerySet [<Question: What's new?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's new?>]>
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
```

Querysets are lazy: the database is only queried when you iterate over them or
print them.


## Admin

Django comes with an admin interface for your models. Register them in
`polls/admin.py`:

```python
from django.contrib import admin

from .models import Choice, Question

admin.site.register(Question)
admin.site.register(Choice)
```

Create an admin (superuser) and log in at `http://127.0.0.1:8000/admin/`:

```shell
$ python manage.py createsuperuser
```


## Other commands

Interactive shell

```shell
$ python manage.py shell
```

Run the tests in all `tests.py` files:

```shell
$ python manage.py test
```

## See also

* [developer.mozilla.org/en-US/…/Server-side/Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
* [Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/), the official tutorial
