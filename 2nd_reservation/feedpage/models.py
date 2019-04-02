from django.db import models
from faker import Faker
from django.utils import timezone

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=256)
    address = models.TextField()
    content = models.TextField()

    # def update_date(self): # 나중에 수정할 때 씀
    #     self.updated_at = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title

    def seed(count): # 추가
            myfake = Faker('ko_KR')
            for i in range(count):
                Place.objects.create(
                    title=myfake.building_name(),
                    address=myfake.land_address(),
                    content=myfake.catch_phrase(),
                )

class Book(models.Model):
    username = models.TextField()
    created_at = timezone.now()
    checkindate = models.DateTimeField(blank=False, null=False)
    checkoutdate = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.username