from django.db import models
from django.urls import reverse
# from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home")


class Comment(models.Model):
    blogpost = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments',)
    name = models.CharField(max_length=55)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.name)
    