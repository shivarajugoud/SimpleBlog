from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default='Coding stuff')
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='blogposts')
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return str(self.title) + '  |   ' + str(self.author)
    def get_absolute_url(self):
        return reverse('article', args=(str(self.pk)))