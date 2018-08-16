from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm, AlbumForm, PhotoForm
from .models import Album, Photo


def album_create(request):
    if not request.user.is_authenticated:
        return render(request, 'travel/login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            for a in Album.objects.all():
                if a.album_title == form.cleaned_data.get("album_title"):
                    context = {
                        'album': album,
                        'form': form,
                        'error_message': 'Album with same name exists',
                    }
                    return render(request, 'travel/album_form.html', context)
            album.save()
            return render(request, 'travel/details.html', {'album': album})
        context = {
            'form': form,
        }
        return render(request, 'travel/album_form.html', context)


def photo_create(request, album_id):
    form = PhotoForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.album = album
        photo.save()
        return render(request, 'travel/details.html', {'album': album})
    context = {
        'form': form,
    }
    return render(request, 'travel/photo_form.html', context)


def album_delete(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'travel/index.html', {'albums': albums})


def photo_delete(request, album_id, photo_id):
    album = get_object_or_404(Album, pk=album_id)
    photo = Photo.objects.get(pk=photo_id)
    photo.delete()
    return render(request, 'travel/details.html', {'album': album})


def details(request, album_id):
    if not request.user.is_authenticated:
        return render(request, 'travel/login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'travel/details.html', {'album': album, 'user': user})


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'travel/login.html')
    else:
        albums = Album.objects.all()
        return render(request, 'travel/index.html', {'albums': albums})


def user_logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'travel/login.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'travel/index.html', {'albums': albums})
            else:
                return render(request, 'travel/login.html', {'error_message': 'The user is no longer active'})
    return render(request, 'travel/login.html')


def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'travel/index.html', {'albums': albums})
    return render(request, 'travel/registration.html', {'form': form})


def search(request):
    if not request.user.is_authenticated:
        return render(request, 'travel/login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        all_photos = Photo.objects.all()
        query = request.GET.get("q")
        albums = albums.filter(
            Q(album_title__icontains=query)
        ).distinct()
        all_photos = all_photos.filter(
            Q(photo_caption__icontains=query)
        ).distinct()
        context = {
            'albums': albums,
            'photos': all_photos,
        }
        return render(request, 'travel/search.html', context)







































