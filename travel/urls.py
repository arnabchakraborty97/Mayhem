from django.conf.urls import url
from . import views

app_name = 'travel'

urlpatterns = [

    # /travel/
    url(r'^$', views.index, name='index'),

    # /travel/register/
    url(r'^register/$', views.register, name='register'),

    # /travel/login
    url(r'^login/$',views.user_login, name='login'),

    # /travel/logout
    url(r'^logout/$', views.user_logout, name='logout'),

    # travel/search/
    url(r'^search/$', views.search, name='search'),

    # /travel/74/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),

    # /travel/album/add/
    url(r'album/add/$', views.album_create, name='album-add'),

    # /travel/album/photo/add/
    url(r'album/(?P<album_id>[0-9]+)/add/$', views.photo_create, name='photo-add'),

    # /travel/album/id/delete_album/
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.album_delete, name='delete-album'),

    # /travel/album/id/delete_song/id/
    url(r'album/(?P<album_id>[0-9]+)/delete_photo/(?P<photo_id>[0-9]+)/$', views.photo_delete, name='delete-photo'),
]