from django.contrib import admin
from .models import Post, customuser

# Register your models here.
admin.site.register(Post)
admin.site.register(customuser)
