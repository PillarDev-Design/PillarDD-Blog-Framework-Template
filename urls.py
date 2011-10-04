from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pillardd.views.home',  name='home'),
    # url(r'^pillardd/', include('pillardd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Homepage
    url(r'^$', 'mysiteapp.views.home'),

    # Blog directory
    url(r'^blogs/', 'mysiteapp.views.blogdir'),

    # Blog search page
    url(r'^blogsearch/', 'mysiteapp.views.blogsearch'),

    # Wiki directory
    url(r'^wikis/', 'mysiteapp.views.wikidir'),

    # Wiki search page
    url(r'^wikisearch/', 'mysiteapp.views.wikisearch'),

    # Wiki edit request page
    url(r'^wikiedit/', 'mysiteapp.views.wikiedit'),

    # Tutorials directory
    url(r'^tutorials/', 'mysiteapp.views.tutorialdir'),

    # Tutorial search page
    url(r'^tutorialsearch/', 'mysiteapp.views.tutorialsearch'),

    # About page
    url(r'^about/', 'mysiteapp.views.about'),

    # Pulls blog by a slug
    url(r'^blog/(?P<target_slug>.+)/$', 'mysiteapp.views.get_blog'),

    # Pulls wiki by a slug
    url(r'^wiki/(?P<target_slug>.+)/$', 'mysiteapp.views.get_wiki'),

    # Pulls a wiki edit request by a slug
    url(r'^editrequest/(?P<target_slug>.+)/$', 'mysiteapp.views.editrequest'),

    # Pulls a tutorial by a slug
    url(r'^tutorial/(?P<target_slug>.+)/$', 'mysiteapp.views.get_tutorial'),
)

urlpatterns += patterns('',url(r'^staticfiles/(?P<path>.*)$',
    'django.views.static.serve', {'document_root':'data/www',
        'show_indexes':True}),)
