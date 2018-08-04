#-*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django import template
from django.views.generic import ListView,TemplateView,DetailView
from blog.models import Carousel,Article
# Create your views here.

class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self,**kwargs):
        kwargs['website_title'] = "My Test Blog"

        #轮播
        kwargs['carousel_page_list'] = Carousel.objects.all()
        return super(IndexView,self).get_context_data(**kwargs)

		
class ArticleView(DetailView):
    queryset = Article.objects.all()
    template_name = 'blog/content.html'
    context_object_name = 'article'

    def get(self,request,*args,**kwargs):
        pk_value = int(self.kwargs.get(self.pk_url_kwarg,None))

        #article = self.queryset.get(pk=1)
        article = get_object_or_404(Article, pk=pk_value)

        return super(ArticleView,self).get(request,*args,**kwargs)
