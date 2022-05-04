from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings

# Create your models here.
""" class User(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True, default='')
    surname = models.CharField(max_length=50, blank=True, default='')
    mail = models.EmailField(max_length=150)
    pw = models.CharField(max_length=50)

    class Meta:
        ordering = ['id'] """

class Railway(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, default='')
    description = models.CharField(max_length=650, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, default='')
    url = models.CharField(max_length=150, blank=True, default='')
    description = models.CharField(max_length=650, blank=True, default='')
    duration = models.IntegerField(default=1000)
    railway = models.ForeignKey(Railway, on_delete=models.CASCADE, related_name='videoOfRailway')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    answerOne = models.TextField(default='')
    answerTwo = models.TextField(default='')
    answerThree = models.TextField(default='')
    correct = models.TextField(default='')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='questionOfVideo')

    class Meta:
        ordering = ['id']

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='ResultOfQuestions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ResultOfUser')

    class Meta:
        ordering = ['id']
