#-*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django import template
from django.views.generic import ListView,TemplateView,DetailView
from blog.models import Carousel,Article
from django.conf import settings
from django.http import Http404
# Create your views here.

class BaseMixin(object):
    def get_context_data(self,*args,**kwargs):
        context = super(BaseMixin,self).get_context_data(**kwargs)
        try:
            #the title
            context['website_title'] = settings.WEBSITE_TITLE

            #the hot article
            context['hot_article_list'] = Article.objects.order_by("-view_times")[0:10]
        except Exception as e:
            print("load basic error") 

        return context       

class IndexView(BaseMixin, TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self,**kwargs):
        #kwargs['website_title'] = "My Test Blog"

        #轮播
        kwargs['carousel_page_list'] = Carousel.objects.all()
        return super(IndexView,self).get_context_data(**kwargs)


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
            article.view_times += 1
            article.save()    
                

        return super(ArticleView,self).get(request,*args,**kwargs)
