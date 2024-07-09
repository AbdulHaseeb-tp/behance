from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/',  views.login, name='login'),
    path('logout/',  views.logoutUser, name='logout')
]
