from pyexpat import model
from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'published_date', 'content']
    list_display_links = ['title', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'content']

    class meta:
        model = Post


admin.site.register(Post, PostAdmin)
