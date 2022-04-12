from django.shortcuts import redirect, render
import json
from django.contrib.auth.models import User
from .models import Profile, Project


from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProjectSerializer, ProfileSerializer

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    projects = Project.get_projects()
    return render(request, 'index.html', {'title': 'Home', 'projects': projects})


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    print(profile.user.username)
    projects = Project.objects.filter(user=profile)
    return render(request, 'profile.html', {'title': 'Profile', 'profile': profile, 'projects': projects})


# Helper function to create profile
def create_profile(user):
    try:
        # If profile is created, get the profile
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # If profile is not created, create a new profile
        profile = Profile(user=user)
        profile.save_user()

    return profile


def edit_profile(request):
    user = request.user
    # Test if profile is created
    profile = create_profile(user)

    if request.method == 'POST':
        bio = request.POST['bio_info']

        # check if profile pic is uploaded to update if not use the default or the old one
        try:
            file = request.FILES['profile_pic']
        except:
            file = profile.profile_pic

        # Test if profile is created
        profile = Profile.objects.get(user=user)
        profile.bio = bio
        profile.profile_pic = file
        profile.save()

    return render(request, 'edit_profile.html', {'title': 'Edit Profile', 'profile': profile})


def submit_project(request):
    user = request.user
    profile = create_profile(user)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        link = request.POST['link']
        image = request.FILES['image']
        category = request.POST['category']
        rating = 0

        project = Project(title=title, description=description,
                          link=link, image=image, category=category, rating=rating, user=profile)
        project.save_project()

    return render(request, 'submit_project.html', {'title': 'Submit Project'})


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project_detail.html', {'title': 'Project Detail', 'project': project})


def rate_project(request, pk):
    if request.method == 'POST':
        print('***********************************************')
        rating = json.loads(request.body)['rating']
        id = json.loads(request.body)['pk']
        project = Project.objects.get(id=id)
        project.rating = float(rating)
        project.save_project()

    return render(request, 'project_detail.html', {'title': 'Project Detail'})

    # print(project.rating)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def logout(request):
	
	return redirect(request,"index.html")