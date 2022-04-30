from rest_framework import serializers
from api.models import User, Question, Result, Video


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class RailwaySerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = '__all__'
    depth = 2

class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = '__all__'
    depth = 1

class QuestionSerializer(serializers.ModelSerializer):
  id_video = VideoSerializer()

  class Meta:
    model = Question
    fields = '__all__'
    depth = 2

class ResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = '__all__'
