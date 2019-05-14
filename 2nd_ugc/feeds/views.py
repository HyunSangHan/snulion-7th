from django.shortcuts import render, redirect
from .models import Feed, FeedComment, CommentReply
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q

# from django.contrib import auth

# Create your views here.
def index(request):
    # 로그인 한 경우에만 index를 렌더해주려면 어떻게 하지?
    keyword = request.GET.get('keyword', '')
    feeds_all = Feed.objects.all().order_by('-updated_at', '-created_at')
    if keyword: 
        feeds_all = feeds_all.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(writer__icontains=keyword))
    search_result_num = len(feeds_all)

    paginator = Paginator(feeds_all, 10)
    page_num = request.GET.get('page')
    feeds = paginator.get_page(page_num)

    if keyword and feeds:
        is_searched = True
    elif keyword == '':
        is_searched = False
    else:
        is_searched = True
    return render(request, 'feeds/index.html', {'feeds' : feeds, 'keyword' : keyword, 'is_searched' : is_searched, 'search_result_num' : search_result_num})

def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        writer = request.POST['writer']
        content = request.POST['content']
        img = request.FILES.get('img', False)

        Feed.objects.create(title=title, content=content, category=category, writer=writer, img=img)
        return redirect('/')
    else:
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
        keyword = request.GET.get('keyword', '')
        feeds_all = Feed.objects.filter(category = category).order_by('-updated_at', '-created_at')
        if keyword: 
            feeds_all = feeds_all.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(writer__icontains=keyword))
        paginator = Paginator(feeds_all, 10)
        page_num = request.GET.get('page')
        feeds = paginator.get_page(page_num)

        return render(request, 'feeds/category.html', {'feeds' : feeds, 'category' : category})

    else:
        return redirect(request.META['HTTP_REFERER'])

def show(request, id):
    feed = Feed.objects.get(id=id)
    if request.method == 'POST':
        feed.title = request.POST['title']
        feed.category = request.POST['category']
        feed.writer = request.POST['writer']
        feed.content = request.POST['content']
        img = request.FILES.get('img', False)
        feed.updated_at = timezone.now()
        feed.save()
        return redirect('/article/%d/'%id)
    else:
        feed.view_count += 1
        feed.save()
        return render(request, 'feeds/show.html', {'feed': feed})

def manage(request, id):
    feed = Feed.objects.get(id=id)
    if (request.method == 'POST') and (feed.password == request.POST['password']) :
        #  일단 렌더를 통해 구현했음!
        # return redirect('/article/%d/edit/'%id)
        return render(request, 'feeds/edit.html', {'feed': feed})  
    else:
        return render(request, 'feeds/manage.html', {'feed': feed})

# def edit(request, id):
#     feed = Feed.objects.get(id=id)
#     return render(request, 'feeds/edit.html', {'feed': feed})    

def delete(request, id):
    if request.method == "POST":
        feed = Feed.objects.get(id=id)
        feed.delete()
        return redirect('/')
    else:
        return redirect('/')

def create_comment(request, id):
    reactor = request.POST['reactor']
    password = request.POST['password']
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, reactor=reactor, password=password, content=content)
    return redirect(request.META['HTTP_REFERER'])

def delete_comment(request, id, cid):
    if request.method == "POST":
        c = FeedComment.objects.get(id=cid)
        if c.password == request.POST['password']:
            c.delete()
            return redirect('/article/%d/'%id)
        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'feeds/manage_comment.html', {'id':id, 'cid':cid})

def create_reply(request, id, cid):
    replyer = request.POST['replyer']
    password = request.POST['password']
    content = request.POST['content']
    CommentReply.objects.create(feed_comment_id=cid, replyer=replyer, password=password, content=content)
    return redirect(request.META['HTTP_REFERER'])

def delete_reply(request, id, cid, rid):
    if request.method == 'POST':
        r = CommentReply.objects.get(id=rid)
        if r.password == request.POST['password']:
            r.delete()
            return redirect('/article/%d/'%id)
        else:
            return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'feeds/manage_reply.html', {'id':id, 'cid':cid, 'rid':rid})