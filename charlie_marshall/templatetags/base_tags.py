from django import template
from photologue.models import Photo

register = template.Library()

@register.filter(name='picture')
def picture(value):
	return Photo.objects.get(title_slug=value).get_thumbnail_url()
