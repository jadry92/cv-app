""" This forms are to verify the user input and to create the user input form. """

# Django
from django import forms
from django.conf import settings

# models
from job.models import Job, JobDetails


class JobModelForm(forms.ModelForm):

    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS
    )
    date_applied = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS
    )

    class Meta:

        model = Job
        fields = ["name", "url", "status", "cv", "cover_letter", "date_applied", "deadline"]
