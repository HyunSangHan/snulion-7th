from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        if password == request.POST['password2']:
            user = User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    else:
        return render(request, 'accounts/login.html')

def profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        current_password = request.POST['current_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
# 디폴트 밸류 값 넣기
        if user.check_password(current_password) and (password1 == password2) :
            # good case
            if password1 != '':
                user.set_password(password1)
            user.username = request.POST['username']
            user.save()
            profile.birthday = request.POST['birthday']
            profile.is_male = request.POST['gender']
            profile.left_level = request.POST['politics']
            profile.save()
            return redirect('/')

        else:
            # for error message
            if user.check_password(current_password) == False :
                error_msg = 'Check your current password'
            elif password1 != password2 :
                error_msg = 'Check your new password'
            elif password1 == '' :
                error_msg = 'Check your new password. It is empty value!'
            else :
                error_msg = 'Unexpected error! Please tell us about this error case'
            return render(request, 'accounts/profile.html', {'profile': profile, 'error': error_msg})

    return render(request, 'accounts/profile.html', {'profile': profile}) #for GET method