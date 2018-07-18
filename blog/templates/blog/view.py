#-*- coding:utf-8 -*-

from django import template

class IndexView(ListView):
	template_name = 'blog/index.html'

	def get_context_data(self,**kwargs):
		kwargs['website_title'] = "My Test Blog"
		return super(IndexView,self).get_context_data(**kwargs)

		