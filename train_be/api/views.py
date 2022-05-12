from rest_framework import generics

from .models import Video, Question
from .serializer import VideoSerializer


class videoDetail(generics.RetrieveAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

class videoCreate(generics.CreateAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

class videoList(generics.ListAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

""" send the object with the key: values you want to change """
class videoUpdate(generics.UpdateAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    return super().perform_update(serializer)

class videoQuestionlist(generics.ListAPIView):
  lookup_field = 'pk'
  queryset = Question.objects.prefetch_related('video').filter(video=pk)
  res = []
  for q in queryset:
    res.append({'question-id': q.id, 'video-id': q.video.id,'text': q.text, 'answerOne': q.answerOne, 'answerTwo': q.answerTwo, 'answerThree': q.answerThree, 'correct': q.correct})