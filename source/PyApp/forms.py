from django import forms
from .models import AuthUser

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = AuthUser
		fields=["firstname","lastname","email","age","gender"]
		# fields="__all__"