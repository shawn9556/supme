from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=32)
    nickname=models.CharField(max_length=64)
    phonenumber=models.CharField(max_length=32)
    emailadress=models.CharField(max_length=64)
    adresshome=models.CharField(max_length=128)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
