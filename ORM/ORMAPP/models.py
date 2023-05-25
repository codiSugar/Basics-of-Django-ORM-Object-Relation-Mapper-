from django.db import models

# Create your models here.




class Catogory(models.Model):
    moviename = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    
    
    
class Post(models.Model):
    genres = models.CharField(max_length=50)
    body = models.TextField(max_length=50000)