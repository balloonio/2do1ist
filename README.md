# Todolist in Django

This is a basic Django based todo-list web app.

## Setup environment

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

## Create Django project

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

## Create Django app

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

```py
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
