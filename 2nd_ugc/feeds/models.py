from django.db import models
from django.utils import timezone
from faker import Faker
# from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import MaxValueValidator, MinValueValidator
import random
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=10)
    password = models.TextField(default='1234') # have to fix (for privacy and default)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def seed(count):
            myfake = Faker('ko_KR')
            for i in range(count):
                rand = random.randrange(1,9)
                if rand == 1:
                    tmp = '연예'
                elif rand == 2:
                    tmp = '스포츠'
                elif rand == 3:
                    tmp = '정치'
                elif rand == 4:
                    tmp = '경제'
                elif rand == 5:
                    tmp = '사회'
                elif rand == 6:
                    tmp = '생활/문화'
                elif rand == 7:
                    tmp = '세계'
                else:
                    tmp = 'IT/과학'
                Feed.objects.create(
                    title=myfake.bs(),
                    category = tmp,
                    writer=myfake.name(),
                    content=myfake.catch_phrase() + ' 속에 ' + myfake.catch_phrase() + ' 제시',
                )