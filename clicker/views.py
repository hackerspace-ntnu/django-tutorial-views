from django.http import HttpResponse
from django.shortcuts import render

def helloWord(request):
    return HttpResponse('Hello World!')
