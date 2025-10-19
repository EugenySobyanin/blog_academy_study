from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    """Форма для создания публикаций."""

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')


class CommentForm(forms.ModelForm):
    """Форма для создания комментраиев."""

    class Meta:
        model = Comment
        fields = ('text',)
