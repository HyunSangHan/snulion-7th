from django.db import models
from django.utils import timezone
from faker import Faker
from django.core.validators import MaxValueValidator, MinValueValidator
import random
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=10)
    password = models.TextField(default='1234') # have to fix (for privacy and default)
    view_count = models.IntegerField(default=0)
    writer = models.CharField(max_length=10)
    content = models.TextField()
    img = models.ImageField(null=True, upload_to='feed_photos')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    # class Meta:
    #     ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.title

    def seed(count):
            myfake = Faker('ko_KR')
            for i in range(count):
                rand = random.randrange(1,9)
                if rand == 1:
                    category = '연예'
                elif rand == 2:
                    category = '스포츠'
                elif rand == 3:
                    category = '정치'
                elif rand == 4:
                    category = '경제'
                elif rand == 5:
                    category = '사회'
                elif rand == 6:
                    category = '생활/문화'
                elif rand == 7:
                    category = '세계'
                else:
                    category = 'IT/과학'
                Feed.objects.create(
                    title=myfake.bs(),
                    category = category,
                    writer=myfake.name(),
                    content=myfake.catch_phrase() + ' 속에 ' + myfake.catch_phrase() + ' 제시 ' + myfake.catch_phrase(),
                )

class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    reactor = models.CharField(max_length=10)
    password = models.TextField(default='1234') # have to fix (for privacy and default)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reactor
        
class CommentReply(models.Model):
    content = models.TextField()
    feed_comment = models.ForeignKey(FeedComment, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=10)
    password = models.TextField(default='1234') # have to fix (for privacy and default)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.replyer