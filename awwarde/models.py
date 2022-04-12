from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pics', default='profile_pics/default.svg')

    bio = models.TextField(blank=True)

    def save_user(self):
        self.save()

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='projects',null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=100)
    rating = models.DecimalField(default=0, decimal_places=1, max_digits=3)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects