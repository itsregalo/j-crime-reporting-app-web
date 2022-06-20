from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


User = settings.AUTH_USER_MODEL
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    ver_code = models.CharField(blank=True, null=True, max_length=10)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
