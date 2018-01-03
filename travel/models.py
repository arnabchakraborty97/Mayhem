from django.db import models


class Album(models.Model):
    album_title = models.CharField(max_length=500)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title


class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo_file = models.FileField()
