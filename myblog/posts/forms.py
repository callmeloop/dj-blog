from django import forms
from .models import *
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    userName = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    title = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    content = RichTextField()

    class Meta:
        model  = Post
        fields = ('userName','title','content',)
