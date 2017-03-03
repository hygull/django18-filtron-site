	
from django.shortcuts import render
from .models import AuthUser, Post
from .forms import UserRegistrationForm, ImagePostingForm
from django.core.files.images import get_image_dimensions
# Create your views here.

def home(request):
	return render(request,"home.html",{})

def registration(request):
	form = UserRegistrationForm(request.POST)
	if form.is_valid():
		form.save(commit=True)
	return render(request,"registration.html",{"form":form})

def order_by_firstname(request):
	users=AuthUser.objects.all().order_by("firstname");
	return render(request,"auth_users.html",{"users":users,"order":"Order by firstname"})

def auth_users(request):
	users=AuthUser.objects.all()
	return render(request,"auth_users.html",{"users":users,"order":"Order by registration"})

def image_posts(request):
	posts = Post.objects.all().order_by("-created_at")
	return render(request,"image_posts.html",{"posts":posts})

def post_a_new_image(request):
	if request.method=="POST":
		form = ImagePostingForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			print "Creating a new post(images)"
			img = form.cleaned_data["image"]
			print img,type(img)
			dimension = get_image_dimensions(img)
			if dimension[0]<1200:
				print "Image width should be >= 1200"
				return render(request,"error.html",{"dimension_err":"Image width should be >= 1200<br><br>Current width : "+str(dimension[0])+"<br><br>Current resolution : "+str(dimension[0])+"x"+str(dimension[1])})
			else:
				if dimension[1]<800:
					print "Image height should be >= 800"
					return render(request,"error.html",{"dimension_err":"Image height should be >= 800<br><br>Current height : "+str(dimension[1])+"<br><br>Current resolution : "+str(dimension[0])+"x"+str(dimension[1])})
				else:
					form.save(commit=True)
			return render(request,"success.html",{})
		else:
			print "Form is not valid"
			print request.POST
			return render(request,"error.html",{})
	else:
		form = ImagePostingForm()
		return render(request,"post_a_new_image.html",{"form":form})

def success(request):
	return render(request,"success.html",{})

def error(request):
	return render(request,"error.html",{})