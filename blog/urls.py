from django.conf.url import url
from blog.views import IndexView

urlpatterns = [
		url(r'^$',IndexView.as_view(),name='index-view'),
]