from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput
            (attrs={'class': 'form-title', 'placeholder': 'Enter the title'}),
            'content': forms.Textarea
            (attrs={'class': 'form-content', 'placeholder': 'Enter the content'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea
            (attrs={'class': 'form-comment', 'placeholder': 'Enter the comment'}),
        }
