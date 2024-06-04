from django.db import models
# from django.contrib.auth.models import User

class Recipes(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()  # Ensure this line is present
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)


    def __str__(self) :
        return str(self.id)
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)