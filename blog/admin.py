from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'author',
        'date_created',
        'main_image'
    )

    ordering = ['-date_created']


admin.site.register(Blog, BlogAdmin)
