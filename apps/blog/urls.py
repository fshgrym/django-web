#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
#time:'2018/2/3 11:24:24上午'
from django.conf.urls import url
from .views import IndexView,ArchivesView,ShowView,TagView,CategoryView,SearchView,LoginView,RegisterView,LogoutView
urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),

    url(r'^post/(?P<id>\d+)/$',ShowView.as_view(),name='post'),
    url(r'^tag/(?P<id>\d+)/$',TagView.as_view(),name='tag'),
    url(r'^category/(?P<id>\d+)/$',CategoryView.as_view(),name='category'),
    url(r'^comment/(?P<id>\d+)/$',ShowView.as_view(),name='comment'),
    url(r'^search/$',SearchView.as_view(),name='search'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^logout/$',LogoutView.as_view(),name='user_logout'),

    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),
    url(r'^archives/$',ArchivesView.as_view(),name='archives_all')
]