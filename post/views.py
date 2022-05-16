from django.shortcuts import render, HttpResponse


def index_view(request):
    return HttpResponse("Sample")


def create_view(request):
    return HttpResponse("Sample")


def detail_view(request):
    return HttpResponse("Sample")


def update_view(request):
    return HttpResponse("Sample")


def delete_view(request):
    return HttpResponse("Sample")
