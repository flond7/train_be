from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True, default='')
    surname = models.CharField(max_length=50, blank=True, default='')
    mail = models.EmailField(max_length=150)
    pw = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    correct = models.BooleanField()
    id_question = models.IntegerField()
    id_user = models.IntegerField()  

    class Meta:
        ordering = ['id']

class Railway(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, default='')

    class Meta:
        ordering = ['id']

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, default='')
    url = models.CharField(max_length=150, blank=True, default='')
    duration = models.IntegerField()  
    id_railway = models.ForeignKey(Railway, on_delete=models.CASCADE, related_name='related_vid')

    class Meta:
        ordering = ['id']

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    answerOne = models.TextField(default='')
    answerTwo = models.TextField(default='')
    answerThree = models.TextField(default='')
    correct = models.TextField(default='')
    id_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='related_quest')

    class Meta:
        ordering = ['id']