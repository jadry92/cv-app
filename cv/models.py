""" This file contains the model for the CV """

# Django imports
from django.db import models

# Models
from users.models import User, ProfilePicture, Skill, Experience, Education, Project, AboutMe, SocialNetwork


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cv")
    name = models.CharField(max_length=255)
    profile_picture = models.ForeignKey(
        ProfilePicture, on_delete=models.SET_NULL, related_name="cv", null=True, blank=True
    )
    skills = models.ManyToManyField(Skill, related_name="cv")
    experiences = models.ManyToManyField(Experience, related_name="cv")
    educations = models.ManyToManyField(Education, related_name="cv")
    projects = models.ManyToManyField(Project, related_name="cv")
    social_networks = models.ManyToManyField(SocialNetwork, related_name="cv")
    about_me = models.ForeignKey(AboutMe, on_delete=models.SET_NULL, related_name="cv", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return name and description."""
        return f"{self.name}"

    def get_cv_str(self):
        """Return a string representation of the cv."""

        experiences = "\n".join([f"-{exp.description}" for exp in self.experiences.all()])
        educations = "\n".join([f"-{edu.degree}" for edu in self.educations.all()])
        skills = "\n".join([f"-{skill.name}" for skill in self.skills.all()])
        return f"""
        Name: \n {self.user.first_name} {self.user.last_name}
        Experience: \n {experiences}
        Education: \n {educations}
        Skills: \n {skills}
        """


class CVTemplate(models.Model):
    cv = models.ManyToManyField(CV, related_name="template")
    name = models.CharField(max_length=255, unique=True)
    template_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
