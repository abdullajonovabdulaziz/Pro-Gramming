from django.db import models
from django.db.models import *


# Create your models here.
class Card(models.Model):
    image=models.ImageField(upload_to='card/image/')
    title=models.CharField(max_length=255, unique=True)
    subtitle=models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
class Theme(models.Model):
    title=models.CharField(max_length=150)
    card=models.ForeignKey(Card,on_delete=models.CASCADE, related_name='mavzular')

    def __str__(self):
        return self.title

class Video(models.Model):
    image=models.ImageField(upload_to='video/images')
    video=models.FileField(upload_to='video/videos')
    title=models.CharField(max_length=150)
    card=models.ForeignKey(Theme,on_delete=CASCADE, related_name='videolar')

class Test(models.Model):
    title=models.CharField(max_length=150)
    batafsil=models.TextField(max_length=250)

    def __str__(self):
        return self.title