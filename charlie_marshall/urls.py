from django.conf.urls import patterns, include, url
from django.contrib import admin
from home.views import home
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', home, name='home'),
	url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^photologue/', include('photologue.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
)
