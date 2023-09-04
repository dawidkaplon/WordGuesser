from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('words/get', views.GetWord.as_view()),
    path('words/list/get', views.GetList.as_view()),
    path('words/get/<int:id>', views.GetWordDetails.as_view()),
    path('words/add', views.AddWord.as_view()),
]