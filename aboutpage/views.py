from django.shortcuts import render, HttpResponse


def about(request):
    return HttpResponse('<h1>Nothing For now! </h1>')
