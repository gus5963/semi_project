"""MBTIgg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from MBTIgg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('istj/', include('hobbyApp.urls')),
    path('intp/', include('hobbyApp.urls')),
    path('istp/', include('hobbyApp.urls')),
    path('intj/', include('hobbyApp.urls')),
    path('isfj/', include('hobbyApp.urls')),
    path('isfp/', include('hobbyApp.urls')),
    path('infp/', include('hobbyApp.urls')),
    path('infj/', include('hobbyApp.urls')),
    path('estj/', include('hobbyApp.urls')),
    path('estp/', include('hobbyApp.urls')),
    path('entj/', include('hobbyApp.urls')),
    path('entp/', include('hobbyApp.urls')),
    path('esfj/', include('hobbyApp.urls')),
    path('esfp/', include('hobbyApp.urls')),
    path('enfj/', include('hobbyApp.urls')),
    path('enfp/', include('hobbyApp.urls')),

]

