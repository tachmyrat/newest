from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200, blank=True )
    body= RichTextField()
    photo= models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
        
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  # Replace 'your_app.Post' with your actual Post model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')  
#class Comment(models.Model):
  #  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
# comment = models.CharField(max_length=150)
 # 3  author = models.ForeignKey(
  #      get_user_model(),
   #     on_delete=models.CASCADE,
   # )
   # def __str__(self):
   #     return self.comment
    #def get_absolute_url(self):
   #     return reverse('article_list')