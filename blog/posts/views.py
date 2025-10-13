from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('about')

def posts(request: HttpRequest) -> HttpResponse:
    return HttpResponse('posts')

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('login')
