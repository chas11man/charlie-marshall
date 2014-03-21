from django.contrib import admin
from polls.models import Blog_Post

class Blog_PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog_Post, Blog_PostAdmin)
