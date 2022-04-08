
# Create your views here.
from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,SignupForm, PostForm, UpdateUserForm, UpdateUserProfileForm, RatingsForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Rating
from .seralizers import ProfileSerializer, UserSerializer, PostSerializer
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random

def index(request):
	if request.method == "POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=request.user
			post.save()

	else:
		form=PostForm()

	try:
		posts=Post.objects.all()
		posts=posts[::-1]
		a_post=random.randint(0, len(posts)-1)
		random_post=posts[a_post]
		print(random_post.photo)
	except Post.DoesNotExist:
		posts=None

		return render (request,"index.html", {'posts':posts, 'form':form,'random_post':random_post})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})
