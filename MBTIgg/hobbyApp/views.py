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
    # join에서 해당 user_id를 갖고 있는 사람의 이름을 찾는 방법!!!!!!!!
    hobby_all = Hobby.objects.select_related('user_id').all()
    for hobby in hobby_all:
        print(hobby.user_id.name)
    context={
        'mbti_id' : mbti_id,
        'hobbys' : hobbys,
        'mbti_table' : mbti_table,
        'user_mbti' : user_mbti,
        'user_name': user_name,
    }
    return render(request, 'hobby.html',context)


def rmdSubmit(request):
    print('✅ GET Hobby Submit 🚀')
