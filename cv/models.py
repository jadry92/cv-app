""" This file contains the model for hte CV """

# Django imports
from django.db import models

# Local imports
from users.models import User, ProfilePicture, Skill, Experience, Education, Project, AboutMe

class CV(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cv')
    name = models.CharField(max_length=255)
    profile_picture = models.ForeignKey(ProfilePicture, on_delete=models.CASCADE, related_name='cv')
    skills = models.ManyToManyField(Skill, related_name='cv')
    experiences = models.ManyToManyField(Experience, related_name='cv')
    educations = models.ManyToManyField(Education, related_name='cv')
    projects = models.ManyToManyField(Project, related_name='cv')
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='cv')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user', 'name']
        verbose_name = 'CV'
        verbose_name_plural = 'CVs'
