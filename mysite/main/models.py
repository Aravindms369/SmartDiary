from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    writer = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    public_or_private = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class search(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title