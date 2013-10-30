from django.conf.urls import patterns, include, url
from Informations import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Informations.views',
    (r'^information/$', 'display_information'),
    (r'^information/add/', 'add'),
    # Examples:
    # url(r'^$', 'MyColleagues.views.home', name='home'),
    # url(r'^MyColleagues/', include('MyColleagues.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
