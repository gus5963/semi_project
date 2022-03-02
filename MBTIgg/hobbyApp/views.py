from django.shortcuts import render

# Create your views here.


def index(request):
    print('✅ GET Hobby Index 🚀')
    return render(request, 'hobby/index.html')