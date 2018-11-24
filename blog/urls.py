from django.conf.urls import url
from blog.views import IndexView,ArticleView,CommentView,ZanView,google_yanzheng
from django.views.generic import TemplateView

urlpatterns = [
		url(r'^$',IndexView.as_view(),name='index-view'),
        url(r'^blog/(?P<pk>\d+).html$',ArticleView.as_view(),name='article-detail-view'),
        url(r'^comment/(?P<pk>\d+)',CommentView.as_view()),
        url(r'^zan',ZanView.as_view()),
        url(r'^change-password$',TemplateView.as_view(template_name="blog/change_passwd.html"),name="change-posswd-view"),
        url(r'^googlef5c50adcb3c8f8e0.html$',google_yanzheng),
]