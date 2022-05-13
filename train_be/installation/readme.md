# first time manually create the data in the admin panel then dump the tables to have the test data
- to dump a table use dumpdata appName.modelName
- jsons will be created in the main directory

## GROUPS & USERS
- python manage.py dumpdata auth.Group --indent 4 > group.json
- python manage.py dumpdata auth.User --indent 4 > users.json

## API MODELS
- python manage.py dumpdata api.question --indent 4 > questions.json
- python manage.py dumpdata api.video --indent 4 > video.json
...

# Load
- python manage.py loaddata group.json
...


# ERROR: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
- open the json file in notepad, save as utf-8




# open python shell
- python manage.py shell.

# run the script
- python installation/script.py



https://suyojtamrakar.medium.com/how-to-provide-initial-data-in-django-models-2422aaf3c09a
