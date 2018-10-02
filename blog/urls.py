from django.conf.urls import url
from blog.views import IndexView,ArticleView,CommentView,ZanView

urlpatterns = [
		url(r'^$',IndexView.as_view(),name='index-view'),
        url(r'^blog/(?P<pk>\d+).html$',ArticleView.as_view(),name='article-detail-view'),
        url(r'^comment/(?P<pk>\d+)',CommentView.as_view()),
        url(r'^zan',ZanView.as_view()),
]