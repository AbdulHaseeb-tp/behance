from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from . models import Profile
from django.contrib.auth.models import User


def createProfile(sender, instance, created, **kwargs):
    print("user created")
    if created:
        user = instance
        profile = Profile.objects.create(user=user, name=user.first_name)

post_save.connect(createProfile, sender=User)        