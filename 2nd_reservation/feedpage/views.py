from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    return render(request, 'feedpage/home.html')

def detail(request):
    return render(request, 'feedpage/detail.html')