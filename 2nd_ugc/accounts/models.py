from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=False, null=True)
    is_male = models.BooleanField(blank=False, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()
    # 합쳐질지 확인 필요