from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.title
        
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)


class CustomUser(AbstractUser):
        def __str__(self):
            return self.username

        nickname = models.CharField(max_length=20)
        phone_number = models.CharField(max_length=20)