from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.


def index_view(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {"posts": posts})


def create_view(request):
    return HttpResponse("Create")


def detail_view(request):
    return HttpResponse("Detail")


def update_view(request):
    return HttpResponse("Update")


def delete_view(request):
    return HttpResponse("Delete")
