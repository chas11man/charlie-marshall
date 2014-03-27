from django.db import models
from django.template import Context, Template
from django.template.defaultfilters import slugify
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
	posted = models.DateTimeField(auto_now_add=True)

	def posted_date(self):
		return self.posted.strftime('%B %d, %Y')

	@property
	def template(self):
		return Template(self.body)

	@property
	def render(self):
		t = self.get_template()
		c = Context({'post': self})
		return t.render(c)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Blog_Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
