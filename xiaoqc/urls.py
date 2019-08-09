"""xiaoqc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from blog import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('mdeditor/', include('mdeditor.urls')),
    path('detail/<str:blog_url>/', views.detail),
    path('tags/', views.tags),
    path('tag/<str:tag_name>/', views.tag),
    path('categories/<str:cate_name>/', views.cate),
    path('categories/', views.categories),
    path('wechat/', views.wechat),
]

handler404 = "blog.views.page_not_found"

if True:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
