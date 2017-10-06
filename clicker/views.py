from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from clicker.models import Clicker

def increaseClicks(request, clicker_id):
    clicker_id = int(clicker_id)
    if Clicker.objects.filter(pk=clicker_id).exists():
        clicker = Clicker.objects.get(pk=clicker_id)
        clicker.clicks += 1
        clicker.save()

    return HttpResponseRedirect('/')


def showClicks(request):
    context = {
        'clickers': Clicker.objects.all()
    }

    return render(request, 'clicker/clicks.html', context)
