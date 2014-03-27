from django.http import Http404
from django.shortcuts import render, redirect
from blog.models import Blog_Post

def blog_helper(request, posts, page=1):
	if len(posts) == 0:
		if page == 1:
			raise Http404
		else:
			page -= 1;
			return redirect('blog_paged', page=page)
	elif len(posts) < 6:
		next_page = False
	else:
		next_page = True
		posts = posts[:5]

	months = {}
	for post in Blog_Post.objects.all().order_by('-posted'):
		if post.posted.strftime('%B \'%y') not in months:
			months[post.posted.strftime('%m%y')] = post.posted.strftime('%B \'%y')

	context = {'posts': posts, 'page': page, 'next_page': next_page, 'months': months, }
	return render(request, 'blog.html', context)


def blog(request):
	posts = Blog_Post.objects.all().order_by('-posted')[:6]

	return blog_helper(request, posts)

def blog_paged(request, page):
	page = int(page)
	if page <= 1:
		return redirect('blog')

	end_post = (page - 1) * 5
	posts = Blog_Post.objects.all().order_by('-posted')[end_post:end_post+6]

	return blog_helper(request, posts, page)

def blog_month(request, month):
	mon = month[:2]
	year = month[2:]
	posts = Blog_Post.objects.filter(posted__year='20{0}'.format(year), posted__month='{0}'.format(mon)).order_by('-posted')[:6]

	return blog_helper(request, posts)

def blog_month_paged(request, month, page):
	page = int(page)
	if page <= 1:
		return redirect('blog_month', month=month)

	end_post = (page - 1) * 5
	mon = month[:2]
	year = month[2:]
	posts = Blog_Post.objects.filter(posted__year='20{0}'.format(year), posted__month='{0}'.format(mon)).order_by('-posted')[end_post:end_post+6]

	return blog_helper(request, posts, page)
