from unicodedata import name
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post_description, name="postdesc"),
    path('createpost/', views.createpost, name='createpost')
]
