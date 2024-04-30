# Python Backend

# Django Architecture
* like we have MVC (model view controller) in other backend frameworks,
Model (for data)
View (the html format we see on the screen)
Controller (for operations)(work as a request handler) 

* In django, we have MTV (model template view)
Model (for data)
Template (the html format we see on the screen)
View (for operations/logic)(work as a request handler)


# django populrity
* less time & less code
* Youtube, instagram, spotify, dropbox

# django features
* admin site (for data management)
* object relational mapper - ORM (abstracts data from database)(it is a database abstraction API)(every user is an object, while tables in the database are known as relations)
* Authentication (for identifying users)
* Caching (for caching the data)


# how web works
* client requests a url(endpoint) from the server, in return, the server fetch and send data from database to the client, and client generate html document to see that data on his web page.
* endpoints (/product, /orders) act like an interface that client use to talk to the server. Or simply saying, server provides API to the client(like a remote button that a client can click to access something).


# django environment setup(Windows)
- virtualenv myenv
- .\myenv\Scripts\activate   OR  workon myenv
- pip install django
- dango-admin --version


# creating django project
- django-admin startproject myproject .
- python manage.py help
- python manage.py runserver
* delete the sessions app from INSTALLED-APPS headline at path /myproject/settings.py

# craeting django app
- python manage.py startapp myapp
* register the calc app in INSTALLED-APPS headline at path /myproject/settings.py

# writing views (request -> response)
* views module is a request handler
* the purpose of views module in calc app is to take a request and return a response

# mapping URLs to views
* urls.py in calc app is the url configuration file for the current app
* another urls.py inside the firstProj project is the URL configuration for storefront project.

# using templates DTL (django template language)
* what we call 'views' in other frameworks are called 'templates' in django
* create a templates folder inside the main directory
* register the templates as base directory in the TEMPLATES headline at path /firstProj/settings.py


# craete another app named 'mytravello'
- python manage.py startapp mytravello
* paste the index.html file  in templates folder and the supporting data associated with it in templates and static folders.
* update the urls.py and views.py files with new data
* now update the urls.py file inside the main project named 'firstProj'
* download free frontend template from dhiWise website
* register the static as base directory in the STATICFILES_DIRS headline at path /firstProj/settings.py
* add static root and create a new folder named 'assets' through it
- python manage.py collectstatic
* update the templates/index.html file to django format


# passing dynamic data using jinja format



# DB/models
* download postgresql install & pgadmin 
* postgres port (5432)
* Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- pip install psycopg2
- pip insall pillow
* register your database in settings file
- python manage.py makemigrations
- python manage.py sqlmigrate travello 0001
- python manage.py migrate
* Now check the Databases/myproject1/Schemas/public/Tables/travello_destination inside pgadmin4 to see the changes. A new table is just created with the name 'travello_destination'

# re-migration
- python manage.py makemigrations
- python manage.py migrate

# create a super user at /admin
- python manage.py createsuperuser
* register your model class in travello.admin file


# fetch and add data from database
* to upload images through database, register media root and url inside settings file
* now register this media path in projet's url file

# craete a separate app for user account data(login, register, logout)
- python manage.py startapp accounts
* by default, django gives us a user database inside the tables folder in postgres database with the name 'auth_user'




# Requirements.txt file (contains all the required package names)
- pip install -r requirements.txt



