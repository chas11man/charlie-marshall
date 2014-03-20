from django.shortcuts import render
from photologue.models import Photo

def home(request):
    return render(request, 'index.html', {'photo': Photo.objects.all()[0].image.url})
