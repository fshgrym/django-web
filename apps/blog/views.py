# -*- coding:utf-8 -*-
import json
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,render_to_response
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout  #登入和登出
from django.contrib.auth.decorators import login_required  # 验证用户是否登录
from django.db.models import Q
# from django.utils import reverse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Article,Banner,Tag,Comment,Links,Category
from .form import CommentForm,RegisterForm,LoginForm

import markdown
# Create your views here.

class TagView(View):
    def get(self,request,id):
        links = Links.objects.all()
        tag = get_object_or_404(Tag,id=id)
        all_article = Article.objects.filter(tags=tag).order_by('-create_time')
        comments_set = set()
        all_comment = Comment.objects.all()
        for i in all_comment:
            comments = i.article
            comments_set.add(comments)
        comments_list = list(comments_set)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article,5, request=request)
        all_article = p.page(page)

        return render(request, 'list.html',{'tag':tag,
                                'all_article':all_article,
                                'comments':comments_list,
                                'links':links
                                           })
class ArchivesView(View):
    '''归档'''
    def get(self,request):
        links = Links.objects.all()
        comments_set = set()
        all_comment = Comment.objects.all()
        for i in all_comment:
            comments = i.article
            comments_set.add(comments)
        comments_list = list(comments_set)

        return render(request,'archives.html',{'comments':comments_list,
                             'links':links})
# class ArchivesView(View):
#     '''归档'''
#     def get(self,request,year,month):
#         links = Links.objects.all()
#
#         comments_set = set()
#         all_comment = Comment.objects.all()
#         for i in all_comment:
#             comments = i.article
#             comments_set.add(comments)
#         comments_list = list(comments_set)
#
#         post_list = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
#         try:
#             page = request.GET.get('page', 1)
#         except PageNotAnInteger:
#             page = 1
#         p = Paginator(post_list,5, request=request)
#         all_article = p.page(page)
#
#         return render(request, 'list.html',{
#                                 'all_article':all_article,
#                                 'comments':comments_list,
#                                 'links':links
#                                            })
class CategoryView(View):
    def get(self,request,id):
        links = Links.objects.all()
        cate = get_object_or_404(Category,id=id)
        all_article = Article.objects.filter(category=cate).order_by('-create_time')

        comments_set = set()
        all_comment = Comment.objects.all()
        for i in all_comment:
            comments = i.article
            comments_set.add(comments)
        comments_list = list(comments_set)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article,5, request=request)
        all_article = p.page(page)

        return render(request, 'list.html',{
                                'all_article':all_article,
                                'comments':comments_list,
                                'links':links
                                      })
from django import forms
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20)
class SearchView(View):
    def get(self,request):
        search_form = SearchForm()
        if search_form.is_valid():
            keyword=search_form.cleaned_data.get('keyword')
        links = Links.objects.all()
        keyword = request.GET.get('keyword','')
        all_article = Article.objects.filter(Q(title__icontains=keyword)|Q(body__icontains=keyword))

        comments_set = set()
        all_comment = Comment.objects.all()
        for i in all_comment:
            comments = i.article
            comments_set.add(comments)
        comments_list = list(comments_set)
        #分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article,5, request=request)
        all_article = p.page(page)

        return render(request, 'list.html', {
            'keyword':keyword,
            'search_form':search_form,
                                             'all_article': all_article,
                                             'comments': comments_list,
                                             'links': links
                                             })
class IndexView(View):
    def get(self, request):
        links = Links.objects.all()
        is_tab = Category.objects.filter(is_tab=True)
        all_banner = Banner.objects.all().order_by('-index')[:5]
        all_article = Article.objects.all().order_by('-create_time')
        '''推荐'''
        recom_article = Article.objects.filter(recom=True).order_by('-view')[:1]
        '''最新评论'''

        comments_set = set()
        all_comment = Comment.objects.all()[:5]
        for i in all_comment:
            comments = i.article
            comments_set.add(comments)
        comments_list=list(comments_set)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article,5, request=request)
        all_article = p.page(page)
        #是否主页推荐
        related_article = Article.objects.filter(is_related=True)
        #获取文章最多的分类
        # top_article = Article.objects.all(Category__name=)['']
        return render(request, 'index.html',{
            'all_article':all_article,
            'all_banner':all_banner,
            'recom_article':recom_article,
            'comments':comments_list,
            'links':links,
            'related_article':related_article,
            'is_tab':is_tab
        })


# class ListView(View):
#     def get(self, request):
#         return render(request, 'list.html')


class ShowView(View):
    def get(self,request,id):
        links = Links.objects.all()
        post = get_object_or_404(Article,id=id)
        # post.body = markdown.markdown(post.body,
        #                               extensions=[
        #                                   'markdown.extensions.extra',
        #                                   'markdown.extensions.codehilite',
        #                                   'markdown.extensions.toc',
        #                               ])
        #评论
        comments_set = set()
        all_comment = Comment.objects.all()[:5]
        for i in all_comment:
            comments = i.article
            comments_set.add(comments)
        comments_list = list(comments_set)

        #相关推荐
        cat = post.category
        related_article = Article.objects.filter(category=cat)[:8]

        comment = post.comment_set.all()
        post.view +=1
        post.save()
        return render(request, 'show.html',{'post':post,'comments_list':comment,'comments':comments_list,'links':links,'related_article':related_article})
    def post(self,request,id):
        post = get_object_or_404(Article,id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment.article = post
            comment.save()
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json')

        else:
            return HttpResponse('{"status":"fail","msg":"评论失败"}', content_type="application/json")

# class CommentView(View):
#
def page_not_fount(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response
def page_error(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response
class LoginView(View):
    def get(self,request):
        login_form = LoginForm()
        return render(request,'login.html',{'login_form':login_form})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    msg = '该用户未激活'
                    return render(request,'login.html',{'msg':msg})
            else:
                msg = '用户名密码错误'
                return render(request, 'login.html', {'msg': msg,'login_form':login_form})
        else:
            msg = '用户名密码错误'
            return render(request, 'login.html', {'msg': msg,'login_form':login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html',{'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username','')
            email = register_form.cleaned_data.get('email','')
            password = register_form.cleaned_data.get('password')
            password1 = register_form.cleaned_data.get('password1')
            if User.objects.filter(Q(email=email)|Q(username=username)):
                return render(request, 'register.html', {'register_form': register_form,'email_msg':'邮箱用户名已经存在'})
            elif password!=password1:
                return render(request, 'register.html', {'register_form': register_form, 'pwd_msg': '密码不一致'})
            user = User()
            user.username = username
            user.email = email
            user.password = make_password(password)
            user.save()
            return render(request,'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form, 'msg': '注册失败'})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


