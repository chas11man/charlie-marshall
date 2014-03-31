from .helpers import redirect_url
from django.shortcuts import render
from blog.models import Blog_Post

def blog(request):
	page = int(request.GET.get('page', 1))
	if page < 1:
		return redirect_url(1)
	month = request.GET.get('month', None)
	start = (page - 1) * 5
	if month:
		mon = month[:2]
		year = month[2:]
		posts = Blog_Post.objects.filter(posted__year='20{0}'.format(year), posted__month='{0}'.format(mon)).order_by('-posted')[start:start+6]
	else:
		posts = Blog_Post.objects.all().order_by('-posted')[start:start+6]

	if len(posts) == 0:
		if page == 1:
			raise Http404
		else:
			return redirect_url(page-1, month=month)
	elif len(posts) < 6:
		next_page = False
	else:
		next_page = True
		posts = posts[:5]

	months = {}
	for post in Blog_Post.objects.all().order_by('-posted'):
		if post.posted.strftime('%B \'%y') not in months:
			months[post.posted.strftime('%m%y')] = post.posted.strftime('%B \'%y')

	context = {'posts': posts, 'page': page, 'next_page': next_page, 'months': months, 'month': month}

	return render(request, 'blog.html', context)
