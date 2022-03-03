from django.urls import path, include
from mbtiApp import views

urlpatterns = [
    path('', views.hobby),
    path('hobby/', include('hobbyApp.urls'))
]
