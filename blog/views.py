from django.shortcuts import render, get_list_or_404, get_object_or_404
from blog.models import Blog
from blog.models import Tag
from blog.models import Category
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.


def index(request):
    blogs = get_list_or_404(Blog)
    return render(request, 'blog/list.html', {'blogs' : blogs})


def detail(request, blog_url=None):
    blog = get_object_or_404(Blog, url=blog_url)
    blog.views += 1
    blog.save()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    blog.content = md.convert(blog.content)
    return render(request, 'blog/detail.html', {'blog': blog, 'toc': md.toc})


def tags(request):
    tag_list = get_list_or_404(Tag)
    tag_count = len(tag_list)
    return render(request, 'blog/tags.html', {'tags': tag_list, 'count': tag_count})


def tag(request, tag_name=None):
    tag = get_object_or_404(Tag, url=tag_name)
    blogs = get_list_or_404(Blog, tag=tag.id)
    return render(request, 'blog/tag_list.html', {'blogs': blogs, 'tag': tag})

def cate(request, cate_name=None):
    category = get_object_or_404(Category, url=cate_name)
    blogs = get_list_or_404(Blog, category=category.id)
    return render(request, 'blog/categories.html', {'blogs': blogs, 'cate': category})

def categories(request):
    category_list = get_list_or_404(Category)
    category_count = len(category_list)
    return render(request, 'blog/categories_list.html', {'category_list': category_list, 'count': category_count})

def page_not_found(request):
    return render(request, 'status/404.html')
