from django import forms
from . import models

class ArticlesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea', 'size': '40'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

    class Meta:
        model = models.Article
        fields = ['title', 'text', 'slug', 'thumb']


from crud.models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'textarea',
        'size': '40',
        'placeholder': 'Write your comment here...'
    }))

    class Meta:
        model = Comment
        fields = ['body', ]