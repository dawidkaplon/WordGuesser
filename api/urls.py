from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('words/get', views.get_single_word),
    path('words/list/get', views.get_all_words),
    path('words/add', views.add_word),
    path('words/get/<int:id>', views.word_details),
]