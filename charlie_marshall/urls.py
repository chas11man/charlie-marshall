from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^photologue/', include('photologue.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
)
