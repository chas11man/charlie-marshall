from django.shortcuts import render
from polls.models import Blog_Post

def home(request, page=1):
	page = int(page)
	if page < 1:
		page = 1
	end_post = (page * 5)
	posts = Blog_Post.objects.all().order_by('posted')[end_post-5:end_post]
	if len(posts) < 5:
		end = True
	else:
		end = False
	return render(request, 'index.html', {'posts': posts, 'page': page, 'end': end,})
