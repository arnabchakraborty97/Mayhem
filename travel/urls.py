from django.conf.urls import url
from . import views

app_name = 'travel'

urlpatterns = [

    # /travel/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /travel/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /travel/74/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    # /travel/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /travel/album/photo/add/
    url(r'album/(?P<pk>[0-9]+)/add/$', views.PhotoCreate.as_view(), name='photo-add'),

]