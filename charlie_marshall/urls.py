from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^photologue/', include('photologue.urls')),
)
