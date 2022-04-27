from rest_framework import serializers
from api.models import User, Question, Result


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
  
class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = '__all__'  

class ResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = '__all__'