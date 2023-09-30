from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('words/get/length:<int:length>', views.GetWord.as_view()),
    path('words/list', views.GetList.as_view()),
    path('words/details/<int:id>', views.GetWordDetails.as_view()),
    path('words/add', views.AddWord.as_view()),
]