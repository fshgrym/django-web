#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
# time:'2018/2/3 12:03:51下午'
from .models import Article, Tag, Banner, Category, Comment,Links
import xadmin
from xadmin import views


class ArticleAdmin(object):
    list_display = ['title', 'body', 'excerpt', 'create_time', 'update_time', 'category', 'tags', 'author', 'view']
    search_fields = ['title', 'body', 'excerpt', 'category', 'tags', 'author', 'view']
    list_filter = ['title', 'body', 'excerpt', 'create_time', 'update_time', 'category', 'tags', 'author', 'view']
    # style_fields = {'body':'ueditor'}


class TagAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class BannerAdmin(object):
    list_display = ['title','index','active', 'images', 'upload_time']
    search_fields = ['title', 'images']
    list_filter = ['title', 'index','active','images', 'upload_time']


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CommentAdmin(object):
    list_display = ['name', 'email', 'text', 'article', 'create_time']
    search_fields = ['name', 'email', 'text', 'article']
    list_fields = ['name', 'email', 'text', 'article', 'create_time']
class LinksAdmin(object):
    list_display = ['name', 'url' ,'create_time']
    search_fields = ['name', 'url' ]
    list_fields = ['name', 'url' ]

class GlobalSetting(object):
    site_title = 'Awaf L0g System'  # 修改首页标题
    site_footer = 'Awaf_Team'  # 修改首页页脚标题
    # global_search_models = [Host, IDC]


class BaseSetting(object):
    enable_themes = True #开启主题
    use_bootswatch = True


xadmin.sites.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Links, LinksAdmin)
