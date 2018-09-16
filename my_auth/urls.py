#
from django.conf.urls import url
from my_auth.views import UserControl

urlpatterns = [
		url(r'^user/(?P<slug>\w+)$',UserControl.as_view()),
]