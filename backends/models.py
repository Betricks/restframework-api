from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.

class customuser(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(unique=True, null=False, max_length=1000)
	email = models.EmailField(unique=True)

	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']


class Post(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	author = models.ForeignKey(customuser, on_delete=models.CASCADE)
	data_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-data_created']
