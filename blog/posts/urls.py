from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.create, name='add'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('about/', views.about, name='about'),
]