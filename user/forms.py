from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
