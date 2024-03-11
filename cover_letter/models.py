""" this are the modes for the cover letter app. """

# Django
from django.db import models
from django.contrib.auth import get_user_model

# Models
User = get_user_model()


class CoverLetter(models.Model):
    """This class defines the cover letter model."""

    # Fields
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cover_letter")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Methods
    def __str__(self):
        """Return name and description."""
        return f"{self.name}"


class CoverLetterGPT3(models.Model):
    """This class defines the cover letter model."""

    # Fields
    cover_letter = models.ForeignKey(CoverLetter, on_delete=models.CASCADE, related_name="cover_letter_gpt3")
    name = models.CharField(max_length=50)
    text = models.TextField()
    usage = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Methods
    def __str__(self):
        """Return name and description."""
        return f"{self.name}"
