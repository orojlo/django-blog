from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
# Create your views here.


def index_view(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {"posts": posts})


def create_view(request):
    return HttpResponse("Create")


def detail_view(request):
    post = get_object_or_404(Post, id=1)
    return render(request, 'post/detail.html', {"post": post})


def update_view(request):
    return HttpResponse("Update")


def delete_view(request):
    return HttpResponse("Delete")
