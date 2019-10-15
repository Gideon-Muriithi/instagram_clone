from django import forms 
from .models import Comment, Image, Profile
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'post_date', 'profile']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PostIMageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
