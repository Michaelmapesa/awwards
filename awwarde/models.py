from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django import db
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture=models.ImageField(upload_to='images/',default='default.png')
    bio=models.TextField(max_length=500, default="My Bio",blank=True)
    name=models.CharField(max_length=100, blank=True)
    location=models.CharField(max_length=60, blank=True)
    contact=models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    




