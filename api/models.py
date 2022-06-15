from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.TextField()
    category = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    


class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username 