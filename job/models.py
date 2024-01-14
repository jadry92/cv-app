""" This are the models of the job application. """

# Django
from django.db import models


class Job(models.Model):
    """This is the model of the job."""

    name = models.CharField(max_length=50)
    notes = models.TextField()
    url = models.URLField()
    applied = models.BooleanField(default=False)
    status = models.CharField(max_length=50)
    company = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
