from rest_framework import serializers
from api.models import User, Question, Result, Video


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
  
class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = '__all__'  
    depth = 1

class ResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = '__all__'