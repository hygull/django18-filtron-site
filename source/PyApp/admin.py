from django.contrib import admin
from .models import AuthUser,Post
# Register your models here.
""" admin.py module """
class AuthUserAdmin(admin.ModelAdmin):
	list_display=["email","firstname","lastname","age","gender"]
	class Meta:
		model = AuthUser

admin.site.register(AuthUser,AuthUserAdmin)
admin.site.register(Post)