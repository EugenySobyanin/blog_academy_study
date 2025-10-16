from django.db import models
from django.contrib.auth import get_user_model

from .constants import MAX_LENGTH_POST


User = get_user_model()

def post_image_path(instance, filename):
    # posts/image.jpg_123
    return f'posts/{filename}{instance.id}'


class Post(models.Model):
    """Модель публикации."""

    title = models.CharField(
        'Заголовк',
        max_length=MAX_LENGTH_POST,
        db_index=True
    )
    text = models.TextField('Текст поста')
    image = models.ImageField(
        upload_to=post_image_path,
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
        default_related_name = 'posts'

    def __str__(self):
        return self.title
