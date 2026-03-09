from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Service(models.Model):
    thumbnail = models.ImageField(null=True, blank=True,default='blank.jpeg')
    name = models.CharField(max_length=50)
    additional_info = models.CharField(null=True, blank=True, max_length=255)
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

    def __str__(self):
        return self.username

    
class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.comment