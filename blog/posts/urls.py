from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('add/', views.create, name='add'),
    path('post/', views.create, name='create'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
]