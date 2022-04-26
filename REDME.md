# START

Open VS Code, cd into the main folder
- mkdir folder_name (eg: project_folder)
- cd project_folder

Create a virtual environment in the folder (before adding the new django project, it's easier than conficuring a venv after project creation):
- python -m venv name-virtual-environment
- C:\Users\PESSAE\Documents\webserver\django> name-virtual-environment\Scripts\activate

Install django and djangorest (pay attention to eventual proxy)
- pip install --proxy=http://proxy-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:801 django
- pip install djangorestframework

Create the project
-  django-admin startproject project_name 

Create GIT
- git init
- git remote add origin **URL**
- create .gitignore

Create README
- and copy from past projects

Create basic database for users (inside project_name)
- cd project_name
- python manage.py migrate
- python manage.py runserver (just as a test, then CTRL+C)

Create superuser
- python manage.py createsuperuser (administrator - administrator@localhost.com - com04***) http://127.0.0.1:8000/admin/

Run server from cdm (inside project folder)
- python manage.py runserver

Create new app (in project_name)
- python manage.py startapp app_name (eg: api)
- add app-name to INSTALLED APPS in mainProject/mainProject/settings.py
  INSTALLED_APPS = [
    'django.contrib.admin',
    . . .
    'app-name',
  ]
- create a url.py inside app_name (eg: inside api)
In mainProject/mainProject/urls.py
- add include in from django.urls import path, include
- add urls to urlpatterns in the form of path('api/', include('api.urls'))


# Create api service

Create a model and migrate it so the table is created in the db
- Create a model (table structure) in api/models.py
- python manage.py makemigrations                                  (it creates a mainProject/api/migrations/0001_initial.py file and eventually a mainProject/db.sqlite3 if not present)
  to peak at the db see the section below
- python manage.py migrate

Creat a serializer
- create serializer.py in api

Create a view


# CREATE AN API
- requires, model, serializer, view and a migration
- *** IF NOT USING SQLite3 CREATE THE DATABASE HERE, BEFORE MAKING MIGRATIONS ***
- crete a model (table structure) in mainProject/api/models.py
  -- adding blank=True in the model type makes it not required (es: models.EmailField(blank=True))
- make a migration (to create the table) with: python manage.py makemigrations api
  (it creates a mainProject/api/migrations/0001_initial.py file and eventually a mainProject/db.sqlite3 if not present)
  to peak at the db see the section below
  *** REMEMBER THAT WHEN YOU NEED TO UPDATE A MIGRATION (A DB) THE COMMMAND IS: python manage.py migrate ***
  it creates a table that has app-name_model-name (es: api_women)
- create a serializer (transform tables data in python dictionaries - objects) in mainProject/api/serializer.py
  -- serialization is the process of converting a Model to JSON and allows to specify what fields should be present in the JSON representation of the model (so I can drop the _id autoGenereted and use a custom id)
  -- here you can set up custom validatiors and say if a field is required or not
- create a view in mainProject/api/viwes.py
  remember to import the model and the serializer in the view
- create an url path in mainProject/api/urls.py

python manage.py makemigrations





## ADD A NEW FILED TO DB
- add it in the model
- add it in the serializer
- make migration, migrate

## DB PEAKING (SQLITE3)
- if it gives a CommandError: You appear not to have the 'sqlite3' program installed or on your path. copy the sql.exe file in the same folder as manage.py

- cd into mainProject and in a shell type command: python manage.py dbshell
- >>> .tables (to see all tables)
- >>> .schema --indent table-name (see the stricture)
- >>> select * from table-name
https://realpython.com/django-migrations-a-primer/

## DB MONGODB
- Install djnongo using: 
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 djongo
- install the right mongoengine
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 mongoengine
- install the right pymongo versione (eventually remove if its >4.0)
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1 
- in settings.py change the default DATABASE in
  DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': 'w-database',
      }
  }
- in project/app-name/models.py change che import models from django.db to
  from djongo import models
- makemigrations and then migrate to change to mongoDB:
  python manage.py makemigrations
  python manage.py migrate  
  *** REMEMBER: makemigration creates the file to create the tables, migrates actually creates them ***

*** CREATE A SERIALIZER ***
- in project/app-name create a serializer.py file with
  from rest_framework import serializers
  from .models import woman, path

  class womanSerializer(serializers.ModelSerializer):
    class Meta:
      model = woman
      fields = '__all__'
      depth = 1




*** NESTED MODELS ***
- add _id = models.ObjectIdField() to the model fields of the nested model in order to have nested models

*** WITH ERROR NotImplementedError: Database objects do not implement truth value testing or bool(). Please compare with None instead: database is not None ***
- pymongo version might be wrong, use 3.12.1
  pip uninstall pymongo
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1 

*** WITH ERROR cannot be of type "<class \'django.db.models.fields.BigAutoField\'>" ***
- If it's a mega object with nested objects defined as models, remember to add abstract = True to the Meta class, wich means that djongo won't create a new "table" for the model just include the field where you embedded them
- it's best to reset the DB and migrate again by
  -- in migration folder KEEP __init__.py and delete all the other files 
  -- python manage.py makepigrations
  -- python manage.py migrate


## CONSTANTS FILE
To use constants for models, 
- Create a separate file (es modelsConstat)
- Import it on the main models in the form of: from my-app-name.modelConstants import *
  

reset DB
https://dev.to/rawas_aditya/how-to-reset-django-migrations-169o


## MANAGE URLS
- In main project folder urls.py you can link the ursl.py of a specific app within the main project inside urlpatterns in the form:
  path('sample/', include('sample.urls'))
- remember to have include imported at the top:
  from django.urls import path, include
- Create a ursl.py within the app folder to specify urls for the subfolder (the urs will be ip/root-name-main-urls/root-name-app-urls) :
  from django.urls import path
  from . import views
  urlpatterns = [
    path('pageOne', views.pageOneFunction, name='pageOneName'),
  ]
- In settings.py in the main projects add the string with the app name to INSTALLED APPS
  INSTALLED_APPS = [
    'django.contrib.admin',
    . . .
    'sample',
  ]



### CREATE VIEWS
- In the app folder views.py specify the functions that link to the template in the form

def pageOneFunction(request):
    return render(request, 'pageOne.html', {})

- In the app folder create a folder named templates and inside the pageOne.html. It's important to create templates because django will look for it

    sample/templates/pageOne.html



## GITHUB
git init 
git add README.md 
git config --global http.proxy http[s]://username:password@proxyipaddress:portnumber 
git config --global user.name "NICK" 
git config --global user.mail mail@gmail.com 
git config --global user.password ********* 
git commit -m "first commit" 
git branch -M main 
git remote add origin https://github.com/flond7/angular-startingPoint.git 
git push -u origin main

git branch (check branch name)
git branch -mv origin master (change name from origin to master)

git remote -v (check origin)
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git (change repository)



## DJANGO REST FRAMEWORK
- in the api app add models (one table one model) modifying mainProject/api/models.py
- 





## REST
https://www.bezkoder.com/django-angular-crud-rest-framework/

*** WITH ERROR NotImplementedError: Database objects do not implement truth value testing or bool(). Please compare with None instead: database is not None ***
- pymongo version might be wrong, use 3.12.1
  pip uninstall pymongo
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1 

*** WITH ERROR cannot be of type "<class \'django.db.models.fields.BigAutoField\'>" ***
- If it's a mega object with nested objects defined as models, remember to add abstract = True to the Meta class, wich means that djongo won't create a new "table" for the model just include the field where you embedded them
- it's best to reset the DB and migrate again by
  -- in migration folder KEEP __init__.py and delete all the other files 
  -- python manage.py makepigrations
  -- python manage.py migrate


## MODELS SPECIFICS
To use constants for models, 
- Create a separate file (es modelsConstat)
- Import it on the main models in the form of: from my-app-name.modelConstants import *
  

reset DB
https://dev.to/rawas_aditya/how-to-reset-django-migrations-169o


## MANAGE URLS
- In main project folder urls.py you can link the ursl.py of a specific app within the main project inside urlpatterns in the form:
  path('sample/', include('sample.urls'))
- remember to have include imported at the top:
  from django.urls import path, include
- Create a ursl.py within the app folder to specify urls for the subfolder (the urs will be ip/root-name-main-urls/root-name-app-urls) :
  from django.urls import path
  from . import views
  urlpatterns = [
    path('pageOne', views.pageOneFunction, name='pageOneName'),
  ]
- In settings.py in the main projects add the string with the app name to INSTALLED APPS
  INSTALLED_APPS = [
    'django.contrib.admin',
    . . .
    'sample',
  ]



### CREATE VIEWS
- In the app folder views.py specify the functions that link to the template in the form

def pageOneFunction(request):
    return render(request, 'pageOne.html', {})

- In the app folder create a folder named templates and inside the pageOne.html. It's important to create templates because django will look for it

    sample/templates/pageOne.html



## GITHUB
git init 
git add README.md 
git config --global http.proxy http[s]://username:password@proxyipaddress:portnumber 
git config --global user.name "NICK" 
git config --global user.mail mail@gmail.com 
git config --global user.password ********* 
git commit -m "first commit" 
git branch -M main 
git remote add origin https://github.com/flond7/angular-startingPoint.git 
git push -u origin main

git branch (check branch name)
git branch -mv origin master (change name from origin to master)

git remote -v (check origin)
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git (change repository)



## DJANGO REST FRAMEWORK
- in the api app add models (one table one model) modifying mainProject/api/models.py





## REST
https://www.bezkoder.com/django-angular-crud-rest-framework/

 
