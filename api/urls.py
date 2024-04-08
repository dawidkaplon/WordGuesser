from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('<str:language>/words/get/length:<int:length>', views.GetWord.as_view()),
    path('words/list', views.GetList.as_view()),
    path('words/details/<int:id>', views.GetWordDetails.as_view()),
    path('words/add', views.AddWord.as_view()),
    path('words/list/<str:username>', views.GetUserWords.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
