from django.contrib import admin
from blog.models import Blog
from blog.models import Category
from blog.models import Tag

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'views')
    search_fields = ('title', 'url')
    list_filter = ('title', 'url')
    ordering = ('id',)
    filter_horizontal = ('category','tag')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'blog_num')
    search_fields = ('name', 'url')
    list_filter = ('name', 'url')
    ordering = ('id',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'url')
    list_filter = ('name', 'url')
    ordering = ('id',)