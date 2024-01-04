"""This file contains the models for the users app."""

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)


class ProfilePicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_picture')
    picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.picture.name


class AboutMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about_me')
    about = models.TextField(max_length=500, blank=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class SocialNetwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_network')
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill')
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    description = models.TextField(max_length=500, blank=True)
    degree = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    shcool = models.CharField(max_length=50)

    def __str__(self):
        return self.degree


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    description = models.TextField(max_length=500, blank=True)
    title = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    description = models.TextField(max_length=500, blank=True)
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
