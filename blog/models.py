# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

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


class Carousel(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    summary = models.TextField(blank=True,null=True,verbose_name=u'摘要')
    img = models.CharField(max_length=200,verbose_name=u'轮播图片',default='/static/img/carousel/img1.jpg')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'轮播'
        ordering = ['-create_time']
        app_label = string_with_title('blog',u'博客管理')