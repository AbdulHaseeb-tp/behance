from django import forms
from .models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','tags','cover','image1','image2']
         