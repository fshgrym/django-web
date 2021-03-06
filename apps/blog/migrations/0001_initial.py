# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-04 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('body', models.TextField(verbose_name='文章正文')),
                ('recom', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('excerpt', models.CharField(blank=True, max_length=255, verbose_name='文章摘要')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_related', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('view', models.PositiveIntegerField(default=0, verbose_name='访问量')),
                ('image', models.ImageField(blank=True, default='default/default.png', null=True, upload_to='article/%Y/%m', verbose_name='封面图')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('index', models.IntegerField(default=0, verbose_name='优先')),
                ('active', models.CharField(blank=True, max_length=10, null=True, verbose_name='是否为选中状态')),
                ('images', models.ImageField(upload_to='banner/%Y/%m', verbose_name='图片')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名字')),
                ('email', models.EmailField(max_length=255, verbose_name='邮箱')),
                ('text', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='所属文章')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='网站名称')),
                ('url', models.URLField(verbose_name='链接')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签'),
        ),
    ]
