from django.shortcuts import render, redirect
from .models import Feed
from django.utils import timezone
# from django.contrib import auth

# Create your views here.
def index(request):
    # 로그인 한 경우에만 index를 렌더해주려면 어떻게 하지?
    if request.method == 'GET':
        feeds = Feed.objects.all().order_by('-updated_at', '-created_at')
        return render(request, 'feeds/index.html', {'feeds' : feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        writer = request.POST['writer']
        content = request.POST['content']
        img = request.POST['img']
        Feed.objects.create(title=title, content=content, category=category, writer=writer, img=img)
        return redirect('/')

def new(request):
    return render(request, 'feeds/new.html')

def category(request, id):
    if id == 1:
        category = '연예'
    elif id == 2:
        category = '스포츠'
    elif id == 3:
        category = '정치'
    elif id == 4:
        category = '경제'
    elif id == 5:
        category = '사회'
    elif id == 6:
        category = '생활/문화'
    elif id == 7:
        category = '세계'
    elif id == 8:
        category = 'IT/과학'
    else:
        category = None
    
    if category:
        feeds = Feed.objects.filter(category = category).order_by('-updated_at', '-created_at')
        return render(request, 'feeds/category.html', {'feeds' : feeds})
    else:
        return redirect('/')

def show(request, id):
    feed = Feed.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'feeds/show.html', {'feed': feed})
    elif request.method == 'POST':
        feed.title = request.POST['title']
        feed.category = request.POST['category']
        feed.writer = request.POST['writer']
        feed.content = request.POST['content']
        feed.img = request.POST['img']
        feed.updated_at = timezone.now()
        feed.save()
        return redirect('/article/%d/'%id)

def manage(request, id):
    feed = Feed.objects.get(id=id)
    if (request.method == 'POST') and (feed.password == request.POST['password']) :
        return redirect('/article/%d/edit/'%id)
    else:
        return render(request, 'feeds/manage.html', {'feed': feed})

def edit(request, id):
    feed = Feed.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'feeds/edit.html', {'feed': feed})    

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/')