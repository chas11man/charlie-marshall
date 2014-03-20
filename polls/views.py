from django.shortcuts import render
from photologue.models import Photo

def home(request):
	if Photo.objects.all():
		photo = Photo.objects.all()[0].image.url
	else:
		photo = None
	return render(request, 'index.html', {'photo': photo})
