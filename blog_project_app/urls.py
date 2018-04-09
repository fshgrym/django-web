# -*- coding:utf-8 -*-
"""blog_project_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.static import  serve #处理静态文件
from django.conf.urls import url,include
# from django.contrib import admin
import xadmin
from blog_project_app import settings
from blog.feeds import AllPostsRssFeed

urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),
    url(r'',include('blog.urls')),
    url(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#处理上传文件路径,
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),

]
#全局404 500
handler404 = 'blog.views.page_not_fount'
handler500 = 'blog.views.page_error'


from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
