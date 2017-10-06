from django.conf.urls import url

from clicker.views import showClicks, increaseClicks

urlpatterns = [
    url(r'^$', showClicks),
    url(r'^increase/(?P<clicker_name>.*)$', increaseClicks),
]
