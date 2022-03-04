from django.shortcuts import render, redirect
from .models import *
from mbtiApp.models import *
from userApp.models import *

# Create your views here.


def index(request):
    print('✅ GET Hobby Index 🚀')
    mbti_id = request.GET['mbti']
    hobbys = Hobby.objects.all()
    request.session.get('user_mbti')
    request.session.get('user_name')
    context={
        'mbti_id' : mbti_id,
        'hobbys' : hobbys,
    }

    return render(request, 'hobby/index.html',context)


def rmdSubmit(request):
    print('✅ GET Hobby Submit 🚀')
