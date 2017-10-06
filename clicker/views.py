from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from clicker.models import Clicker

def increaseClicks(request, clicker_name):
    if Clicker.objects.filter(name=clicker_name).exists():
        clicker = Clicker.objects.get(name=clicker_name)
    else:
        clicker = Clicker.objects.create(name=clicker_name)

    clicker.clicks += 1
    clicker.save()

    return HttpResponseRedirect('/')


def showClicks(request):
    context = {
        'clickers': Clicker.objects.all()
    }

    return render(request, 'clicker/clicks.html', context)
