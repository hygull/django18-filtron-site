from django.shortcuts import render
from .models import AuthUser
from .forms import UserRegistrationForm
# Create your views here.

def home(request):
	return render(request,"home.html",{})

def registration(request):
	form = UserRegistrationForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
	return render(request,"registration.html",{"form":form})

def auth_users(request):
	users=AuthUser.objects.all()
	return render(request,"auth_users.html",{"users":users})

def image_posts(request):
	return render(request,"image_posts.html",{})
