from django.contrib import admin

from django.contrib import admin
from bloging.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image',)