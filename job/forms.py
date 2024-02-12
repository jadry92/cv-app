""" This forms are to verify the user input and to create the user input form. """

# Django
from django import forms

# models
from job.models import Job, JobDetails


class JobModelForm(forms.ModelForm):

    class Meta:

        model = Job
