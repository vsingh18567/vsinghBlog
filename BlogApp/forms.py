from django import forms
from .models import *

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add post title here'
            }),

            'author': forms.Select(attrs={
                'class': 'form-control'
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'cool content'
            })
        }

class EditForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add post title here'
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'cool content'
            })
        }