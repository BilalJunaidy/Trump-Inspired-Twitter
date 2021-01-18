from django.db import models

# Create your models here.

class Tweet(models.Model):
    content = models.TextField(max_length = 140)
    image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

