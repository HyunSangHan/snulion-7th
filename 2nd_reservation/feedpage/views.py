from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

def home(request):
    users = User.objects.all()
    return render(request, 'feedpage/home.html', {'users' : users})

def detail(request):
    return render(request, 'feedpage/detail.html')