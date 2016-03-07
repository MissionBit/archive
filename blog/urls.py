from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'blog.views.hello', name='hello'),
    url(r'^hello/(?P<yourname>\w+)/$', 'blog.views.hello_name', name='hello_name'),
    url(r'^time/', 'blog.views.time',name ='time'),
    url(r'^favorites/','blog.views.favs',name='favs'),
    url(r'^reviews/','blog.views.all_reviews',name='all_reviews'),
    url(r'^review/new/$', 'blog.views.new_review', name='new_review'),
    url(r'^review/random/', 'blog.views.random', name = 'random'),
    url(r'^review/title/', 'blog.views.by_title', name ='by_title'),
]
