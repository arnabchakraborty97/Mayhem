from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    album_title = models.CharField(max_length=500)
    album_logo = models.ImageField(upload_to='album_logo')

    def get_absolute_url(self):
        return reverse('travel:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo_file = models.ImageField(upload_to='photo_file')
    photo_caption = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('travel:details', kwargs={'pk': self.album.pk})

    def __str__(self):
        return self.photo_caption
