""" Educations Forms """

# Django
from django import forms
from django.conf import settings

# Models
from users.models import Education


class EducationModelForm(forms.ModelForm):
    """Education Model Form"""

    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS
    )

    class Meta:
        model = Education
        fields = ("school", "degree", "location", "description", "start_date", "end_date")
