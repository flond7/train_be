from django.urls import path
from . import views
urlpatterns = [
  path('user-list', views.userList, name="user-list"),                 
  path('user-detail/<str:pk>', views.userDetail, name="user-detail"),  
  path('user-create', views.userCreate, name="user-create"),           
  path('user-update/<str:pk>', views.userUpdate, name="user-update"),  
  path('user-delete/<str:pk>', views.userDelete, name="user-delete"),  
  path('question-list', views.questionList, name="question-list"),                 
  path('question-detail/<str:pk>', views.questionDetail, name="question-detail"),  
  path('question-create', views.questionCreate, name="question-create"),           
  path('question-update/<str:pk>', views.questionUpdate, name="question-update"),  
  path('question-delete/<str:pk>', views.questionDelete, name="question-delete"),  
  path('video-list', views.videoList, name="video-list"),                 
  path('video-detail/<str:pk>', views.videoDetail, name="video-detail"),  
  path('video-create', views.videoCreate, name="video-create"),           
  path('video-update/<str:pk>', views.videoUpdate, name="video-update"),  
  path('video-delete/<str:pk>', views.videoDelete, name="video-delete"),  
]