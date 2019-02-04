# Todolist in Django

This is a basic Django based todo-list web app.

## Setup Environment

Create Python virtual environment:

```bash
python3 -m venv myvenv
```

Activate it:

```bash
source /myvenv/bin/activate
```

Install Django:

```bash
pip3 install django
```

## Create Django Project

Create a Django project:

```bash
django-admin startproject mysite .
```

Now let’s look at what startproject created:

```bash
./
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

> - manage.py: A command-line utility that lets you interact with this Django project in various ways.
> - The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
> - mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package.
> - mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
> - mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
>- mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.

Let’s verify our Django project works:

```bash
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

February 01, 2019 - 15:50:53
Django version 2.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

> Note: Ignore the warning about unapplied database migrations for now.

Now that the server’s running, visit http://127.0.0.1:8000/ with a Web browser. We see a “Congratulations!” page, with a rocket taking off. It worked!

> By default, the runserver command starts the development server on the internal IP at port 8000.

## Create Django App

Now that our environment – a “project” – is set up, let's create our todolist app.

Each application we write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so we can focus on writing code rather than creating directories.

> **Projects vs. apps**
>
> What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

To create our todolist app, make sure we are in the same directory as manage.py and type this command:

```
python manage.py startapp todolist
```

Now our directory looks like this:

```
.
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── todolist
    ├── __init__.py
    ├── admin.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

4 directories, 16 files
```

To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todolist'
)
```

### URL, View and a Minimal Working Website

As mentioned above, urls.py is like a "table of contents". It is a URLconf. Let's create a "table of contents" urls.py for todolist app. For now, let's copy the comment section from mysite/urls.py because the comment helps explain what we are doing here. Please read the comment yourself.

```python
# ./todolist/urls.py
"""mysite URL Configuration
 The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
```

Let's reference this app URLconf in our project URLconf based on the instructions in the comment:

```python
# ./mysite/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')) # add this line (and any import if needed by include)
]
```

Before we complete todolist/urls.py, let's create a view inside todolist/views.py. 

What is a view?

> A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response.

Good! It sounds like exactly what we need:

```python
# ./todolist/views.py
from django.http import HttpResponse
import datetime

def index(request):
    message = "Current Time: {}".format(datetime.datetime.now())
    return HttpResponse(message) 
```

Now it's time to complete todolist/urls.py:

```python
# ./todolist/urls.py
from django.conf.urls import url
from django.urls import path

from todolist import views

urlpatterns = [
    path('', views.index, name='index')
]
```

Let’s verify our code works:

```bash
python manage.py runserver
```

Now that the server’s running, visit http://127.0.0.1:8000/ with a Web browser. We can see the current time on the page!
