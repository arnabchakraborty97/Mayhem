from django.shortcuts import render, get_object_or_404
from .models import Album


def index(request):
    albums = Album.objects.all()
    return render(request, 'travel/index.html', {'albums': albums})


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'travel/details.html', {'album': album})


