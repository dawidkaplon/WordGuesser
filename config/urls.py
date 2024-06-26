"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from register import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', v.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', include('mysite.urls')),
    path('', include('api.urls')),
]

urlpatterns += i18n_patterns (
    path('register/', v.register, name='register'),
    path('', include(('django.contrib.auth.urls', 'auth'), namespace='auth')),
    path('', include(('mysite.urls', 'mysite'), namespace='mysite')),
    path('', include(('api.urls', 'api'), namespace='api')),
)
