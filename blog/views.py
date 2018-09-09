#-*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django import template
from django.views.generic import ListView,TemplateView,DetailView
from blog.models import Carousel,Article,Comment
from django.conf import settings
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import time

# Create your views here.

class BaseMixin(object):
    def get_context_data(self,*args,**kwargs):
        context = super(BaseMixin,self).get_context_data(**kwargs)
        try:
            #the title
            context['website_title'] = settings.WEBSITE_TITLE

            #the hot article
            context['hot_article_list'] = Article.objects.order_by("-view_counter")[0:10]

            #the hot comments
            context['hot_comment_list'] = Comment.objects.all()[0:6]

            now_time = time.strftime('%Y-%m-%d %A',time.localtime(time.time()))
            context['now_time'] = now_time

        except Exception as e:
            print("load basic error") 

        return context       

class IndexView(BaseMixin, ListView):
    template_name = 'blog/index.html'

    def get_context_data(self,**kwargs):
        #kwargs['website_title'] = "My Test Blog"

        #轮播
        kwargs['carousel_page_list'] = Carousel.objects.all()

        article_list = Article.objects.all()
        paginator = Paginator(article_list,6,2)
        pageno = self.request.GET.get('page')

        try:
            contacts = paginator.page(pageno)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        kwargs['contacts'] = contacts
        return super(IndexView,self).get_context_data(**kwargs)

    def get_queryset(self):
        article_list = Article.objects.order_by("-view_counter")[0:5]
        return article_list


class ArticleView(BaseMixin, DetailView):
    queryset = Article.objects.all()
    template_name = 'blog/content.html'
    context_object_name = 'article'

    def get(self,request,*args,**kwargs):
        pk_value = int(self.kwargs.get(self.pk_url_kwarg,None))

        try:
            article = self.queryset.get(pk=pk_value)
            #article = get_object_or_404(Article, pk=pk_value)
        except Article.DoesNotExist:
            raise Http404
        else:
            article.view_counter += 1
            article.save()    
                

        return super(ArticleView,self).get(request,*args,**kwargs)

    def get_context_data(self,*args,**kwargs):
        #comment list
        pk_value = int(self.kwargs.get(self.pk_url_kwarg,None))
        kwargs['comment_list'] = self.queryset.get(pk=pk_value).comment_set.all()

        #the next and previous article
        kwargs['prev_article'] = self.queryset.get(pk=pk_value)

        if pk_value == 1:
            kwargs['prev_article'] = self.queryset.get(pk=pk_value)
        else:
            kwargs['prev_article'] = self.queryset.get(pk=(pk_value-1))

        if pk_value == Article.objects.count():
            kwargs['next_article'] = self.queryset.get(pk=pk_value)
        else:
            kwargs['next_article'] = self.queryset.get(pk=(pk_value+1))

        return super(ArticleView, self).get_context_data(**kwargs)

