from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Post, search
 
# Register your models here.

admin.site.register(Post)
admin.site.register(search)

