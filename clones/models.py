from django.db import models


class Profile(models.Model):
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    bio = models.TextField()



class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=20)
    image_caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField('Profile', default=False, blank=True, related_name='likes')
    comments = models.TextField(max_length=70)

    def __str__(self):
        return self.image_caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
