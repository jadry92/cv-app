""" This are the models of the job application. """

# Django
from django.db import models

# Models
from cover_letter.models import CoverLetter
from cv.models import CV


class Job(models.Model):
    """This is the model of the job."""

    name = models.CharField(max_length=50)
    notes = models.TextField()
    url = models.URLField()
    applied = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    company = models.URLField()
    cover_letter = models.ForeignKey(CoverLetter, on_delete=models.SET_NULL, related_name="job", null=True)
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, related_name="job", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
