from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class Post(models.Model):
    image = models.ImageField(null =True, blank =True )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', null = True ,on_delete=models.SET_NULL)
    creeated_date  = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date  = models.DateTimeField()
    def __str__(self):
        return self.title
class Category(models.Model):
      name = models.CharField(max_length=250)    
      def __str__(self):
           return self.name
