from django.conf.urls import url

from clicker.views import helloWord

urlpatterns = [
    url(r'^', helloWord),
]
