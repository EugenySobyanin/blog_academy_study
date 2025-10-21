from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('add/', views.post_create, name='add'),
    path('<int:post_id>/', views.post_detail, name='detail'),
    path('<int:post_id>/update/', views.post_update, name='update'),
    path('<int:post_id>/delete/', views.post_delete, name='delete'),
    path('<int:post_id>/comments/add/',
         views.comment_create, name='add_comment'),
    path('<int:post_id>/comments/<int:comment_id/delete/',
         views.comment_delete, name='delete_comment'),
    path('profile/', views.profile, name='my_profile'),
    path('profile/<slug:user_slug>/', views.profile, name='profile'),
]