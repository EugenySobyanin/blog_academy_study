from typing import Union

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Prefetch
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .constants import POSTS_PAGINATE_COUNT
from .forms import CommentForm, PostForm
from .models import Comment, Post


def post_list(request: HttpRequest) -> HttpResponse:
    """Получение списка всех публикаций."""
    posts = Post.objects.annotate(
        comments_count=Count('comments')
    ).select_related('author')
    paginator = Paginator(posts, POSTS_PAGINATE_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    }
    return render(request, 'posts/list.html', context=context)


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    """Получение отдельной публикации."""
    post = get_object_or_404(
        Post.objects
        .select_related('author')
        .prefetch_related(
            Prefetch(
                'comments',
                queryset=Comment.objects.select_related('author')
            )
        ),
        pk=post_id
    )
    form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'posts/detail.html', context=context)


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    """Создание публикации."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:detail', form.instance.pk)
        return render(request, 'posts/form.html')
    elif request.method == 'GET':
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/form.html', context=context)


@login_required
def post_update(request: HttpRequest, post_id: int) -> HttpResponse:
    """Обновление публикации."""
    post = get_object_or_404(Post, pk=post_id)

    if post.author != request.user:
        return HttpResponseForbidden("У вас нет прав для редактирования этого поста")

    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('posts:detail', form.instance.pk)
    else:
        return render(request, 'posts/form.html', {'form': form})


@login_required
def post_delete(request: HttpRequest, post_id:int) -> HttpResponse:
    return HttpResponse('Удаление поста.')


@login_required
def profile(request: HttpRequest, user_slug: Union[None, str] = None) -> HttpResponse:
    """Получение всех публикаций текущего пользователя."""
    if user_slug is None:
        posts = Post.objects.filter(author=request.user)
    else:
        posts = Post.objects.filter(author__slug=user_slug)
    paginator = Paginator(posts, POSTS_PAGINATE_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'posts/list.html',
        {'page_obj': page_obj, 'is_paginated': page_obj.has_other_pages()}
    )


@login_required
def comment_create(request: HttpRequest, ) -> HttpResponse:
    pass


@login_required
def comment_delete(request: HttpRequest, ) -> HttpResponse:
    pass
