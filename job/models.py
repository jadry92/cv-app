""" This are the models of the job application. """

# Django
from django.db import models

# Models
from cover_letter.models import CoverLetter
from cv.models import CV

JOB_STATUS = [
    (0, "No Applied"),
    (1, "Applied"),
    (2, "Interview"),
    (3, "Rejected"),
    (4, "Offer"),
    (5, "Accepted"),
    (6, "No call"),
]


class Job(models.Model):
    """This is the model of the job."""

    name = models.CharField(max_length=50)
    url = models.URLField()
    status = models.IntegerField(choices=JOB_STATUS, default=0)
    cover_letter = models.ForeignKey(CoverLetter, on_delete=models.SET_NULL, related_name="job", null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, related_name="job", null=True, blank=True)
    date_applied = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return name of the job."""
        return self.name


class JobDetails(models.Model):
    """This is the model of the job details.
    This model will be populated by an AI and scraping alogrithm
    """

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_details")
    description = models.TextField()
    relevant_info = models.TextField()
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
