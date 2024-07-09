from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from . models import Post
from user.models import Profile
from . forms import PostForm


# Create your views here.

def home(request):
    # p=Post.objects.create(title='graphics')
    # p.save()
    post= Post.objects.all()
    profile=Profile.objects.all()

    context={
        'post' :post,
        'profile' :profile
        }
    return render(request, 'index.html', context)
    
def post_description(request, pk):
    post = Post.objects.get(id=pk)
    context={'post' :post}
    return render(request, 'postdesc.html', context)


def createpost(request):
    profile = request.user.profile
    form = PostForm()
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.save()
            return redirect('home')

    context = {'form' :form}
    return render(request, 'createpost.html', context)