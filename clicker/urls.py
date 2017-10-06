from django.conf.urls import url

from clicker.views import showClicks, increaseClicks

urlpatterns = [
    url(r'^$', showClicks),
    url(r'^increase/(?P<clicker_id>[0-9]*)$', increaseClicks),
]
