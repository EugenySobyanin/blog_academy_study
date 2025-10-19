import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


def avatar_image_path(instance, filename):
    ext = filename.split('.')[-1]
    # Генерация уникального имени
    filename = f'{uuid.uuid4()}.{ext}'
    return f'avatars/{filename}'


class User(AbstractUser):
    """Переопределённая модель пользователя."""

    avatar = models.ImageField(
        upload_to=avatar_image_path,
        default='avatars/default_avatar.webp',
        verbose_name='Аватар'
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        verbose_name='Слаг',
    )

    def save(self, *args, **kwargs):
        # Создаем slug ТОЛЬКО при создании пользователя
        if not self.slug:
            self.slug = self.generate_unique_slug()

        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        """Генерирует уникальный slug на основе username"""
        base_slug = slugify(self.username)
        if not base_slug:  # если username состоит из спецсимволов
            base_slug = "user"

        unique_slug = base_slug
        counter = 1

        # Проверяем уникальность
        while User.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{counter}"
            counter += 1

        return unique_slug
