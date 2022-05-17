from multiprocessing import context
from django.shortcuts import render, HttpResponse


def about(request):
    context = {'About': 'Nothing Not Yet'}
    return render(request, 'about.html', context)
