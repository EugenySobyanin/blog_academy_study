import uuid

from django.db import models
from django.contrib.auth import get_user_model

from .constants import MAX_LENGTH_POST


User = get_user_model()


def post_image_path(instance, filename):
    ext = filename.split('.')[-1]
    # Генерация уникального имени
    filename = f'{uuid.uuid4()}.{ext}'
    return f'posts/{filename}'


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


class Comment(models.Model):
    """Комментарий к публикации."""

    text = models.CharField(
        max_length=5000,
        verbose_name='Текст комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Публикация'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментрарии'
        ordering = ['-created_at']
        default_related_name = 'comments'

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text[:25]}'
