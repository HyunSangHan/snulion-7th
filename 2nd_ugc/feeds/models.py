from django.db import models
from django.utils import timezone
from faker import Faker
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.update_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def seed(count):
            myfake = Faker('ko_KR')
            for i in range(count):
                Feed.objects.create(
                    title=myfake.bs(),
                    content=myfake.text()
                )