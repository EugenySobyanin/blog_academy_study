from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Форма связанная с моделью Post."""

    class Meta:
        model = Post
        fields = ('title', 'text')