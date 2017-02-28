from django import forms
from .models import AuthUser, Post

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = AuthUser
		fields=["firstname","lastname","email","age","gender"]
		# fields="__all__"

class ImagePostingForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","description","image","posted_by"]