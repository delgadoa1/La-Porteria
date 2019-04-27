from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
When a User is saved, send signal received by receiver. Receiver is create_profile func that takes 
all arguments that post_save signal passes. If that user is created, create a profile object with 
user = instance of profile created
"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):     # Create a profile crated for each new user
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

