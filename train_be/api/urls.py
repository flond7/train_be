from django.urls import path
from . import views

urlpatterns = [
  path('test', views.TestAuthView.as_view(), name="test"),

  path('question-detail/<int:pk>/', views.questionDetail.as_view(), name="question-detail"),
  path('question-list/', views.questionList.as_view(), name="question-list"),

  path('video-list/', views.videoList.as_view(), name="video-list"),
  path('video-detail/<int:pk>/', views.videoDetail.as_view(), name="video-detail"),
  path('video-question-list/<int:pk>', views.videoQuestionList, name="video-question-list"),

  path('railway-list/', views.railwayList.as_view(), name="railway-list"),
  path('railway-detail/<int:pk>/', views.railwayDetail.as_view(), name="railway-detail"),
  path('railway-video-list/<int:pk>', views.railwayVideoList, name="railway-video-list"),

  path('user-detail/<int:pk>/', views.userDetail.as_view(), name="user-detail"),
  path('user-update/<int:pk>/', views.userUpdate.as_view(), name="user-update"),
  path('user-results/<int:pk>', views.userResults, name="user-results"),

  path('result-create/', views.resultCreate.as_view(), name="result-create"),
  path('user-result/<int:pk>/', views.resultUpdate.as_view(), name="result-update"),
]

""" urlpatterns = [
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
  path('video-list', views.videoList.as_view(), name="video-list"),
  path('video-detail/<str:pk>', views.videoDetail, name="video-detail"),
  path('video-question-list/<str:pk>', views.videoQuestList, name="video-question-list"),
  path('video-create', views.videoCreate, name="video-create"),
  path('video-update/<str:pk>', views.videoUpdate, name="video-update"),
  path('video-delete/<str:pk>', views.videoDelete, name="video-delete"),
  path('rail-list', views.railList, name="rail-list"),
  path('rail-detail/<str:pk>', views.railDetail, name="rail-detail"),
  path('rail-video-list/<str:pk>', views.railVideoList, name="rail-video-list"),
  path('rail-create', views.railCreate, name="rail-create"),
  path('rail-update/<str:pk>', views.railUpdate, name="rail-update"),
  path('rail-delete/<str:pk>', views.railDelete, name="rail-delete"),
  path('user-results/<str:pk>', views.userResults, name="user-results"),
  path('user-create', views.userCreate, name="user-create"),
  path('user-update/<str:pk>', views.userUpdate, name="user-update"),
  path('user-delete/<str:pk>', views.userDelete, name="user-delete"),
] """
