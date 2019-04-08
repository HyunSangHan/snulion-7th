from django.shortcuts import render, redirect
from .models import Feed

# Create your views here.
def index(request):
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