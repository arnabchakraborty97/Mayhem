from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album, Photo
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'travel/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'travel/details.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title', 'album_logo']


class PhotoCreate(CreateView):
    model = Photo
    fields = ['album', 'photo_file', 'photo_caption']


class UserFormView(View):
    form_class = UserForm
    template_name = 'travel/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

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
                    return redirect('travel:index')

        return render(request, self.template_name, {'form': form})








