""" This are the models of the job application. """

# Django
from django.db import models
from django.contrib.auth import get_user_model

# Models
from cover_letter.models import CoverLetter
from cv.models import CV

# Utils
import json

User = get_user_model()

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    name = models.CharField(max_length=500)
    url = models.URLField()
    status = models.IntegerField(choices=JOB_STATUS, default=0)
    cover_letter = models.ForeignKey(CoverLetter, on_delete=models.SET_NULL, related_name="job", null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, related_name="job", null=True, blank=True)
    date_applied = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

    raw_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return name of the job."""
        return self.name

    class Meta:
        """Meta options."""

        ordering = ["-deadline"]


class JobDetails(models.Model):
    """
    This is the model of the job details.
    This model will be populated by an AI and scraping alogrithm
    """

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_details")
    json_detail = models.TextField()
    usage = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_json_detail(self):
        """Return the json detail."""
        json_analysis = json.loads(self.json_detail)
        return self._json_to_str(json_analysis)

    def _json_to_str(self, json):
        """Return a string representation of the json."""
        resp_str = ""
        for key, value in json.items():
            if isinstance(value, list):
                resp_str += f"{key}: {', '.join(value)}\n"
            elif isinstance(value, dict):
                resp_str += self._json_to_str(value)
            else:
                resp_str += f"{key}: {value}\n"

        return resp_str
