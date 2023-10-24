from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("game/", views.Game.gameplay, name="game"),
    path("statistics/<str:user_email>", views.user_statistics, name="statistics"),
]
