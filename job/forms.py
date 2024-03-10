""" This forms are to verify the user input and to create the user input form. """

# Django
from django import forms
from django.conf import settings

# models
from job.models import Job, JobDetails, JOB_STATUS
from cv.models import CV
from cover_letter.models import CoverLetter


class JobModelForm(forms.ModelForm):

    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS, required=False
    )
    date_applied = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS, required=False
    )

    class Meta:

        model = Job
        fields = ["name", "raw_description", "url", "status", "cv", "cover_letter", "date_applied", "deadline"]


class JobAppliedForm(forms.Form):
    status = forms.ChoiceField(choices=JOB_STATUS, widget=forms.Select(attrs={"class": "form-control"}), required=True)
    cv_used = forms.ModelChoiceField(
        queryset=CV.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), required=True
    )
    cover_letter_used = forms.ModelChoiceField(
        queryset=CoverLetter.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), required=True
    )

    def save(self):
        """This is the save method of the job application."""
        job = Job.objects.get(pk=self.cleaned_data["job_id"])
        job.status = self.cleaned_data["status"]
        job.cv_used = self.cleaned_data["cv_used"]
        job.cover_letter_used = self.cleaned_data["cover_letter_used"]
        job.save()
        return job
