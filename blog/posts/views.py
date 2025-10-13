from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .forms import PostForm
from .models import Post


def list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/list.html', context=context)

def detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context=context)    

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('about')

def posts(request: HttpRequest) -> HttpResponse:
    return HttpResponse('posts')

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('login')

def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return 
        return render(request, 'posts/create.html')