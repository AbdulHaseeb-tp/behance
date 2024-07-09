from imaplib import _Authenticator
from multiprocessing import context
from django.shortcuts import render, redirect
from . forms import CustomCreationForm
from django.contrib.auth import login as auth_login,authenticate,logout
from django.contrib.auth.models import User

# Create your views here.

def registerUser(request):
    form = CustomCreationForm()
    
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            print('login successful')
            
            auth_login(request, user)
            return redirect('home')
        else:
            print('login unsuccessful')
            
    context = {'form': form}
    
    return render(request, 'signup.html', context)  


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        try:
            user = User.objects.get(username=username)
        except:
            print("no user found")
            
        user = authenticate(request, username=username,password=password) 
        
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        
        else:
            print("user not found")
            
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("home")                     