from django import forms 
from .models import Comment, Image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'post_date', 'profile']
    