from django.db import models

# Create your models here.
""" A module named models.py that holds the models definition"""
class AuthUser(models.Model):
	""" A model for storing the details of a user"""
	firstname = models.CharField(max_length=25)
	lastname = models.CharField(max_length=25)
	email=models.EmailField()
	age = models.IntegerField()
	GENDER_CHOICES=(('M',"Male"),
					('F','Female'),
					('O','Other'))
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
	created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)

	"""The complete object will be identified with the value returned by this method"""
	def __unicode__(self):
		return self.firstname+' '+self.lastname

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return "/auth-user/id=%i"%(self.id)
		# return reverse("PyApp.views.home",args=[str(self.id)])

class Post(models.Model):
	""" A model for storing Post details"""
	title=models.CharField(max_length=100)
	description=models.TextField()
	image=models.ImageField(help_text="width should be >= 1200 and height should be >= 800. 1200x800 resolution or greater is ok")
	created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)
	posted_by=models.ForeignKey(AuthUser,on_delete=models.CASCADE)

	""" The complete object will be identified with the value returned by this method"""
	def __unicode__(self):
		return self.title


