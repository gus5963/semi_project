from django.urls import path, include
from hobbyApp import views

urlpatterns = [
    path('', views.index, name = 'hobby_index')
]