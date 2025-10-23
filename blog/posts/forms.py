from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    """Форма для создания публикаций."""

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')


class CommentForm(forms.ModelForm):
    """Форма для создания комментраиев."""

    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Напишите ваш комментарий...',
            'rows': 3,
            'class': 'comment-textarea',
            'style': 'resize: none;',
        }),
        label="",
    )

    class Meta:
        model = Comment
        fields = ('text',)
