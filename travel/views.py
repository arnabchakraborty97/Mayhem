from django.shortcuts import render
from .models import Album


def index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'travel/index.html', context)


def details(request, album_id):
    album = Album.objects.get(pk=album_id)
    context = {
        'album': album,
    }
    return render(request, 'travel/details.html', context)


