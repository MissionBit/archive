from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(r'^$', 'buildup.views.hello', name='hello'),
    url(r'^time/$', 'buildup.views.time', name='time'),
    url(r'^random/$', 'buildup.views.random', name='random'),
    url(r'^hello/(?P<yourname>\w+)/$', 'buildup.views.hello_template', name='hello_template'),
    url(r'^speak/(?P<sentence>\w+)/$', 'buildup.views.speak', name='speak'),
    url(r'^facts/$', 'buildup.views.all_facts', name='all_facts'),
    url(r'^facts/new/$', 'buildup.views.new_fact', name='new_fact'),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
