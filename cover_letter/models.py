""" this are the modes for the cover letter app. """


# Django
from django.db import models


class CoverLetter(models.Model):
    """This class defines the cover letter model."""

    # Fields
    name = models.CharField(max_length=50)
    text = models.TextField()
    url_job = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Methods
    def __str__(self):
        """Return name and description."""
        return f"{self.name}"
