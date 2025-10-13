from django.db import models

from .constants import MAX_LENGTH_POST


class Post(models.Model):
    """Модель публикации."""

    title = models.CharField(
        'Заголовк',
        max_length=MAX_LENGTH_POST,
        db_index=True
    )
    text = models.TextField('Текст поста')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
        default_related_name = 'posts'

    def __str__(self):
        return self.title
