from django.contrib import admin
from .models import User, Railway, Question, Video, Result

# Register your models here.
# it allows to have a user friendly interface to input data in the db

admin.site.register(User)
admin.site.register(Railway)
admin.site.register(Video)
admin.site.register(Question)
admin.site.register(Result)