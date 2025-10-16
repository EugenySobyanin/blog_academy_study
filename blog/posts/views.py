from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .constants import POSTS_PAGINATE_COUNT
from .forms import PostForm
from .models import Post


def list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    paginator = Paginator(posts, POSTS_PAGINATE_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'posts/list.html', context=context)

def detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context=context)    

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('about')

def posts(request: HttpRequest) -> HttpResponse:
    return HttpResponse('posts')

def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(author=request.user)
            return redirect('posts:detail', form.instance.pk)
        return render(request, 'posts/form.html')
    elif request.method == 'GET':
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/form.html', context=context)

def update(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=post, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('posts:detail', form.instance.pk)
    else:
        return render(request, 'posts/form.html', {'form': form})
