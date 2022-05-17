from django.shortcuts import render, HttpResponse

# Create your views here.


def index_view(request):
    return HttpResponse("Index")


def create_view(request):
    return HttpResponse("Create")


def detail_view(request):
    return HttpResponse("Detail")


def update_view(request):
    return HttpResponse("Update")


def delete_view(request):
    return HttpResponse("Delete")
