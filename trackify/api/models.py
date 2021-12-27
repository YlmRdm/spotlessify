from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Track.objects.filter(code=code).count() == 0:
            break

    return code
class Track(models.Model):
    code = models.name = models.CharField(max_length=8, default="", unique=True)
    artist = models.name = models.CharField(max_length=20)
    name = models.name = models.CharField(max_length=24)
    genre = models.name = models.CharField(max_length=24)
    album_image_url = models.URLField()
    preview_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)