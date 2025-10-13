from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
]