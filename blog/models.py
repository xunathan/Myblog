# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class string_with_title(str):
    def __new__(cls,value,title):
        instance = str.__new__(cls,value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self:self
    __deepcopy__ = lambda self,memodict:self


 
STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}     


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)

    content = RichTextField()
    summary = models.TextField(verbose_name=u'摘要')
    view_counter = models.IntegerField(default=0)
    zan_counter = models.IntegerField(default=0)
    #view_times = models.IntegerField(default=0)
    tags = models.CharField(max_length=200,null=True,blank=True,
                            verbose_name=u'标签',help_text=u'用逗号分割')

    img = models.CharField(max_length=200, verbose_name=u'文章缩略图', default='static/img/logo.jpg')

    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    #pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')

    def get_tags(self):
        tag_list = self.tags.split(',')

        while '' in tag_list:
            tag_list.remove('')

        return tag_list

    class Meta:
        ordering = ['-create_time',]

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('article-detail-view',args=(self.pk,))    

    def __unicode__(self):
        return self.title

    __str__ = __unicode__                

class Carousel(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    summary = models.TextField(blank=True,null=True,verbose_name=u'摘要')
    img = models.CharField(max_length=200,verbose_name=u'轮播图片',default='/static/img/carousel/img1.jpg')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    article = models.ForeignKey(Article,null=True)

    class Meta:
        verbose_name_plural = verbose_name = u'轮播'
        ordering = ['-create_time']
        app_label = string_with_title('blog',u'博客管理')




