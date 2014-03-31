from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect

def redirect_url(page, month=None):
	url = reverse('blog.views.blog')
	q = '?page=%s' % page
	if month:
		q += '&month=%s' % month
	url = url + q
	return HttpResponseRedirect(url)
