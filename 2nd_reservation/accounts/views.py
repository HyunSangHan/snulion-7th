from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        if password == request.POST['password2']:
            user = User.objects.create_user(
                username, password
            )
            auth.login(request, user)
            print(user)
            return redirect('home')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        print(1)
        if user is not None:
            print(user)
            print(2)
            auth.login(request, user)
            return redirect('home')
        else:
            print(3)
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    elif request.method == "GET":
        return render(request, 'accounts/login.html')        
    else:
        print(4)
        return render(request, 'accounts/login.html', {'error': 'this is the problem'})
