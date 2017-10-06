from django.conf.urls import url

from clicker.views import showClicks

urlpatterns = [
    url(r'^$', showClicks),
]
