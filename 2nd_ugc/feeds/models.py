from django.db import models
from django.utils import timezone
from faker import Faker
from django.core.validators import MaxValueValidator, MinValueValidator
import random
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=50)
    category = models.IntegerField(
        default=8,
        validators=[MaxValueValidator(8), MinValueValidator(1)]
    )
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
                Feed.objects.create(
                    title=myfake.bs(),
                    category = random.randrange(1,9),
                    writer=myfake.name(),
                    content=myfake.text(),
                )