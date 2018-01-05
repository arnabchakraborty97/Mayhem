from django.contrib.auth.models import User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    album_title = models.CharField(max_length=500)
    album_logo = models.ImageField(upload_to='album_logo')

    def __str__(self):
        return self.album_title


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo_file = models.ImageField(upload_to='photo_file')
    photo_caption = models.CharField(max_length=100)

    def __str__(self):
        return self.photo_caption
