from django.shortcuts import render, HttpResponse


def homepage_view(request):
    return HttpResponse('<h1>Hello From HomePage</h1>')
