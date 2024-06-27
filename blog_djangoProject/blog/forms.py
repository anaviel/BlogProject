from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


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


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter username',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter username',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
    )
