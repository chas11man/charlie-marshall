from django.db import models
from tinymce import models as tinymce_models
from photologue.models import Photo

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

class Resume(models.Model):
	pdf = models.FileField(upload_to='pdfs')
	photos = models.ImageField(upload_to='photos')

class Blog_Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = tinymce_models.HTMLField(blank=True)
	photos = models.ManyToManyField(Photo, blank=True)
	posted = models.DateField(db_index=True, auto_now_add=True)
