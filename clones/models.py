from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=20)
    image_caption = models.CharField(max_length=20)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.CharField()
    comments = models.TextField(max_length=70)

class Profile(models.Model):
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    bio = models.TextField()