from django.shortcuts import render, redirect
from .models import *
from mbtiApp.models import *
from userApp.models import *

# Create your views here.


def index(request):
    print('✅ GET Hobby Index 🚀')
    mbti_id = request.GET['mbti']
    hobbys = Hobby.objects.all()
    mbti_table = Mbti.objects.get(mbti_id=mbti_id)
    user_mbti=request.session.get('user_mbti')
    user_name=request.session.get('user_name')
    context={
        'mbti_id' : mbti_id,
        'hobbys' : hobbys,
        'mbti_table' : mbti_table,
        'user_mbti' : user_mbti,
        'user_name': user_name
    }

    return render(request, 'index.html',context)


def rmdSubmit(request):
    print('✅ GET Hobby Submit 🚀')
