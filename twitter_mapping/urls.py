from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter_mapping.views.home', name='home'),
    # url(r'^twitter_mapping/', include('twitter_mapping.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/(?P<username>.+)/$', 'twitter_app.views.user_details', name="user_details"),
    (r'^', include('twitter_app.urls'))
)
