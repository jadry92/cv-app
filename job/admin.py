""" Admin view for the job app. """

# Django
from django.contrib import admin

# Models
from job.models import Job, JobDetails

admin.site.register(Job)
admin.site.register(JobDetails)
