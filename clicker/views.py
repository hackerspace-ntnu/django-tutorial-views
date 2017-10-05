from django.http import HttpResponse
from django.shortcuts import render

from clicker.models import Clicker


def showClicks(request):
    if not Clicker.objects.exists():
        clicker = Clicker.objects.create()
    else:
        clicker = Clicker.objects.first()

    clicker.clicks += 1
    clicker.save()

    return HttpResponse('Clicks %r' % clicker.clicks)
