from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


from .serializer import UserSerializer, QuestionSerializer, ResultSerializer, VideoSerializer, RailwaySerializer
from .models import User, Question, Result, Video, Railway




class questionList(generics.ListAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class questionDetail(generics.RetrieveAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer



###### VIDEO

class videoDetail(generics.RetrieveAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer
  permission_classes = [IsAuthenticated]

class videoList(generics.ListAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer
  """ authentication_classes = [authentication.SessionAuthentication] """
  permission_classes = [IsAuthenticated]

@api_view(['GET'])
def videoQuestionList(request, pk):
  queryset = Question.objects.prefetch_related('video').filter(video=pk)
  res = []
  for q in queryset:
    res.append({'question-id': q.id, 'video-id': q.video.id,'text': q.text, 'answerOne': q.answerOne, 'answerTwo': q.answerTwo, 'answerThree': q.answerThree, 'correct': q.correct})
  return JsonResponse(res, safe=False)



###### RAILWAYS

class railwayList(generics.ListAPIView):
  queryset = Railway.objects.all()
  serializer_class = RailwaySerializer
  permission_classes = [IsAuthenticated]

class railwayDetail(generics.RetrieveAPIView):
  queryset = Railway.objects.all()
  serializer_class = RailwaySerializer
  permission_classes = [IsAuthenticated]

@api_view(['GET'])
def railwayVideoList(request, pk):
  queryset = Video.objects.prefetch_related('railway').filter(railway=pk)
  res = []
  for q in queryset:
    res.append({'railway-id': q.railway.id, 'video-id': q.id, 'description': q.description, 'url': q.url})
  return JsonResponse(res, safe=False)



###### USER

class userDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  

class userUpdate(generics.UpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = 'pk'

@api_view(['GET'])
def userResults(request, pk):
  queryset = Result.objects.prefetch_related('user').filter(user=pk)
  res = []
  for q in queryset:
    res.append({
      'resultId': q.id,
      'resultCorrect': q.correct,
      'questionId':q.question.id,
      'questionText': q.question.text,
      'videoId': q.question.video.id,
      'videoName': q.question.video.name,
      'railwayId': q.question.video.railway.id,
      'railwayName': q.question.video.railway.name,
      'userId': q.user.id})
  return JsonResponse(res, safe=False)



###### RESULT

class resultCreate(generics.CreateAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer

  """ HOOK TO ADD IMPLICIT INFORMATION that are not sent with the data by the user
  def perform_create(self, serializer):
    serializer.save(user=self.request.user) """

""" send the object with the key: values you want to change """
class resultUpdate(generics.UpdateAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer
  lookup_field = 'pk'

"""  HOOK TO ADD ACTIONS, such us sending a confirmation email to the user
  def perform_update(self, serializer):
    instance = serializer.save() """