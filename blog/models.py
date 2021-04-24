from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from django.urls import reverse

# Create your models here.
class post(models.Model):
    title =models.CharField(max_length=200)
    author = models.ForeignKey("auth.user",on_delete=models.CASCADE)
    body= models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class comment(models.Model): # new
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
    Comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,)
   
    def __str__(self):
        return self.Comment

    def get_absolute_url(self):
        return reverse('home')
    
