from django.db import models

# Create your models here.
class Track(models.Model):
    code = models.name = models.CharField(max_length=8, default="", unique=True)
    artist = models.name = models.CharField(max_length=20)
    name = models.name = models.CharField(max_length=24)
    genre = models.name = models.CharField(max_length=12)
    album_image_url = models.URLField()
    preview_url = models.URLField()
    
    
