from django.shortcuts import render,redirect

# Create your views here.
def hobby(request):
    print('✅ GET Hobby 🚀')
    return redirect('hobby_index')