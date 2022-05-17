from multiprocessing import context
from django.shortcuts import render, HttpResponse


def homepage_view(request):
    context = {'Name': 'John'}
    return render(request, 'home.html', context)
