from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import blog, blog_paged, blog_month, blog_month_paged
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', blog, name='blog'),
	url(r'^page/(?P<page>\d+)/$', blog_paged, name='blog_paged'),
	url(r'^month/(?P<month>\d{4})/$', blog_month, name='blog_month'),
	url(r'^month/(?P<month>\d{4})/page/(?P<page>\d+)/$', blog_month_paged, name='blog_month_paged'),
)
