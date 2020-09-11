from django.urls import path
from polls import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('vote/<int:question_pk>', views.vote, name='vote'),
    path('result/<int:question_pk>', views.result, name='result'),
]