from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'author', 'content', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Заголовок',
            'subtitle': 'Подзаголовок',
            'author': 'Автор',
            'content': 'Текст',
            'genre': 'Жанр',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'content': forms.Textarea(attrs={'class': 'form-control mt-2', 'style': 'min-height: 100px; height: 100px;'}),
        }
        labels = {
            'author': 'Автор',
            'content': 'Комментарий',
        }