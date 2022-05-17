from django.shortcuts import render, HttpResponse


def homepage_view(request):
    return render(request, 'home.html', {})
