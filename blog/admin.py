from django.contrib import admin
from blog.models import Blog_Post

class Blog_PostAdmin(admin.ModelAdmin):
    fields = ('title', 'body', 'photos', )

admin.site.register(Blog_Post, Blog_PostAdmin)
