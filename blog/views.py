#-*- coding:utf-8 -*-
from django.shortcuts import render
from django import template
from django.views.generic import ListView,TemplateView
from blog.models import Carousel
# Create your views here.

class IndexView(TemplateView):
	template_name = 'blog/index.html'

	def get_context_data(self,**kwargs):
		kwargs['website_title'] = "My Test Blog"

        #轮播
        kwargs['carousel_page_list'] = Carousel.objects.all()
		return super(IndexView,self).get_context_data(**kwargs)

		