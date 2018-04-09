# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.core.urlresolvers import reverse



@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类名称')
    is_tab = models.BooleanField(default=False,verbose_name='是否放在导航')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '分类'


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '标签'


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    # body = UEditorField('内容', height=600, width=900,
    #     default=u'', blank=True, imagePath="uploads/images/",
    #     toolbars='besttome', filePath='uploads/files/')
    body = models.TextField(verbose_name='文章正文')
    recom = models.BooleanField(verbose_name='是否推荐',default=False)
    excerpt = models.CharField(max_length=255, blank=True, verbose_name='文章摘要')
    create_time = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, verbose_name='作者')
    is_related = models.BooleanField(default=False,verbose_name='是否推荐')
    view = models.PositiveIntegerField(default=0, verbose_name='访问量')
    image = models.ImageField(upload_to='article/%Y/%m',verbose_name='封面图',default='default/default.png',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'id': self.pk})

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = '文章'


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='名字')
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    text = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    article = models.ForeignKey(Article, verbose_name='所属文章')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = verbose_name = '评论'
        ordering = ['-create_time']


@python_2_unicode_compatible
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    index = models.IntegerField(default=0,verbose_name='优先')
    active = models.CharField(max_length=10,verbose_name='是否为选中状态',null=True,blank=True)
    images = models.ImageField(upload_to='banner/%Y/%m', verbose_name='图片')
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = '轮播图'
@python_2_unicode_compatible
class Links(models.Model):
    name = models.CharField(max_length=100,verbose_name='网站名称')
    url = models.URLField(verbose_name='链接')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural=verbose_name='友情链接'