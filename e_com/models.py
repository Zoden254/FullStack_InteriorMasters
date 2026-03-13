from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from datetime import datetime

# Create your models here.
class Service(models.Model):
    thumbnail = models.ImageField(null=True, blank=True,default='blank.jpeg')
    name = models.CharField(max_length=50)
    additional_info = models.CharField(default="Your imagination, our plan.", blank=True, max_length=255)
    cost_range = models.CharField(max_length=20)
    cost_on_offer = models.CharField(max_length=20, blank=True, null=True)
    max_days = models.CharField(max_length=20)

    def __str__(self):
        return self.name 
    
class Sample(models.Model):
    sample_pic = models.ImageField(null=True, blank=True, default='blank.jpeg')
    sample_name = models.CharField(max_length=50)
    price_on_offer = models.CharField(max_length=20)
    customer_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.sample_name


class User(AbstractUser):
    profile_pic = models.ImageField(blank=True, default="blank_profile.jpg")
    bio = models.TextField(null=True, blank=True)
    user_number = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.username

    
class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.comment

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Service)
    
    def __str__(self):
        return self.user.username
    
class Worker(models.Model):
    ROLES = {
        'HD' : 'Head',
        'CD' : 'Creative Designer',
        'WK' : 'Worker'
    }

    service = models.ManyToManyField(Service)
    role = models.CharField(max_length=2, choices=ROLES, default='WK')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(default='blank_profile.jpg', blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name