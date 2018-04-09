#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
#time:'2018/3/11 14:45:44下午'
from django.contrib.syndication.views import Feed

from .models import Article


class AllPostsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "方少会的博客"

    # 通过聚合阅读器跳转到网站的地址
    link = "/"

    # 显示在聚合阅读器上的描述信息
    # description = "Django 博客教程演示项目测试文章"

    # 需要显示的内容条目
    def items(self):
        return Article.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.body