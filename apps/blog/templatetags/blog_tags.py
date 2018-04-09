#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
#time:'2018/3/4 23:28:35下午'
from django import template
from django.db.models.aggregates import Count


import time,timeago
from datetime import datetime

from ..models import Tag,Category,Article

register = template.Library()

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


@register.filter(name='markdown')  #注册template filter
@stringfilter  #希望字符串作为参数
def custom_markdown(value):
    mark = mark_safe(markdown.markdown(value,
        extensions = [  'markdown.extensions.extra',
                        'markdown.extensions.codehilite',
                        'markdown.extensions.toc',],
                                       #safe_mode=True,
                                       enable_attributes=False))
    return mark

@register.simple_tag
def archives():
    return Article.objects.all()

@register.simple_tag
def get_recent_posts(num=5):
    '''获取访问数前五的文章'''
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=num)

@register.simple_tag
def get_categories():
    #获取所有的分类
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
@register.filter(name='strtime')
def datetime_filter(t):
    # 转换成时间数组
    d = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    # t = int(time.mktime(d))
    now = datetime.now()
    a=timeago.format(d,now,'zh_CN')
    return a
    # delta = int(time.time() - t)
    # if delta < 60:
    #     return u'1分钟前'
    # if delta < 3600:
    #     return u'%s分钟前' % (delta // 60)
    # if delta < 86400:
    #     return u'%s小时前' % (delta // 3600)
    # if delta < 604800 :
    #     return u'%s天前'%(delta // 86400)

    # dt = datetime.fromtimestamp(t)
    # return u"%s年%s月%s日"%(dt.year,dt.month,dt.day)