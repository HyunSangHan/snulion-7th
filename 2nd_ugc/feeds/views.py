from django.shortcuts import render, redirect
from .models import Feed
# from django.contrib import auth

# Create your views here.
def index(request):
    # 로그인 한 경우에만 index를 렌더해주려면 어떻게 하지?
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feeds/index.html', {'feeds' : feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/')

def new(request):
    return render(request, 'feeds/new.html')

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/')