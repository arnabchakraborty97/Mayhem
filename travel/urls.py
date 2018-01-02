from django.conf.urls import url
from . import views

urlpatterns = [

    # /travel/
    url(r'^$', views.index, name='index'),

    # /travel/74/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),

]