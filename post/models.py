from distutils.command.upload import upload
from email.mime import image
from profile import Profile
from turtle import title
from django.db import models
from user.models import Profile

# Create your models here.

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null= True, blank= True)
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to="media", null=True , blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    image1 = models.ImageField(upload_to="media", null=True , blank=True)
    image2 = models.ImageField(upload_to="media", null=True , blank=True)
    
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.title
