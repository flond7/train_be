from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.shortcuts import render

from .serializer import UserSerializer, QuestionSerializer, VideoSerializer, RailwaySerializer
from .models import Railway, User, Question, Result, Video


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  basicApi_urls = {
    'List':'/user-list/',
    'Detail':'/user-detail/<str:pk>',
    'Create':'/user-create/',
    'Update':'/user-update/<str:pk>',
    'Delete':'/user-delete/<str:pk>',
    'List':'/question-list/',
    'Detail':'/question-detail/<str:pk>',
    'Create':'/question-create/',
    'Update':'/question-update/<str:pk>',
    'Delete':'/question-delete/<str:pk>',
  }
  return Response(basicApi_urls)

@api_view(['GET'])
def userList(request):
  w = User.objects.all()
  serializer = UserSerializer(w, many=True)  # many=true returns more objects
  return Response (serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
  w = User.objects.get(id=pk)
  serializer = UserSerializer(w, many=False) # many=false returns one object
  return Response (serializer.data)

@api_view(['POST'])
def userCreate(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['POST'])
def userUpdate(request, pk):
  w = User.objects.get(id=pk)
  serializer = UserSerializer(instance=w, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['DELETE'])
def userDelete(request, pk):
  w = User.objects.get(id=pk)
  w.delete()
  return Response ("Deleted")




###### QUESTIONS

@api_view(['GET'])
def questionList(request):
  w = Question.objects.all()
  serializer = QuestionSerializer(w, many=True)  # many=true returns more objects
  return Response (serializer.data)

@api_view(['GET'])
def questionDetail(request, pk):
  w = Question.objects.get(id=pk)
  serializer = QuestionSerializer(w, many=False) # many=false returns one object
  return Response (serializer.data)

@api_view(['POST'])
def questionCreate(request):
  serializer = QuestionSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['POST'])
def questionUpdate(request, pk):
  w = Question.objects.get(id=pk)
  serializer = QuestionSerializer(instance=w, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['DELETE'])
def questionDelete(request, pk):
  w = Question.objects.get(id=pk)
  w.delete()
  return Response ("Deleted")





###### VIDEO

@api_view(['GET'])
def videoList(request):
  w = Video.objects.all()
  serializer = VideoSerializer(w, many=True)  # many=true returns more objects
  return Response (serializer.data)

@api_view(['GET'])
def videoDetail(request, pk):
  w = Video.objects.get(id=pk)
  serializer = VideoSerializer(w, many=False) # many=false returns one object
  return Response (serializer.data)

@api_view(['GET'])
def videoQuestList(request, pk):
  queryset = Question.objects.select_related('video').filter(id=pk)
  res = []
  for q in queryset:
    res.append({'id': q.id, 'text': q.text, 'answerOne': q.answerOne, 'answerTwo': q.answerTwo, 'answerThree': q.answerThree, 'correct': q.correct})
  return JsonResponse(res, safe=False)

@api_view(['POST'])
def videoCreate(request):
  serializer = VideoSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['POST'])
def videoUpdate(request, pk):
  w = Video.objects.get(id=pk)
  serializer = VideoSerializer(instance=w, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['DELETE'])
def videoDelete(request, pk):
  w = Video.objects.get(id=pk)
  w.delete()
  return Response ("Deleted")





###### RAILWAYS

@api_view(['GET'])
def railList(request):
  w = Railway.objects.all()
  serializer = RailwaySerializer(w, many=True)  # many=true returns more objects
  return Response (serializer.data)

@api_view(['GET'])
def railDetail(request, pk):
  w = Railway.objects.get(id=pk)
  serializer = RailwaySerializer(w, many=False) # many=false returns one object
  return Response (serializer.data)

@api_view(['GET'])
def railVideoList(request, pk):
  w = Railway.objects.get(id=pk).hasVid.all()
  serializer = RailwaySerializer(w, many=True)
  return Response (serializer.data)

@api_view(['POST'])
def railCreate(request):
  serializer = RailwaySerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['POST'])
def railUpdate(request, pk):
  w = Railway.objects.get(id=pk)
  serializer = RailwaySerializer(instance=w, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['DELETE'])
def railDelete(request, pk):
  w = Railway.objects.get(id=pk)
  w.delete()
  return Response ("Deleted")
