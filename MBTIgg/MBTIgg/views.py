from django.shortcuts import render
from mbtiApp.models import *
# Create your views here.

def home(request):
    print('✅ GET Home 🚀')
    # orm - select
    mbtis = Mbti.objects.all()
    context = {
        'mbtis':mbtis
    }
    print('mbti',mbtis)
    return render(request, 'home.html', context)