""" Experience Form """

# Django
from django import forms
from django.conf import settings

# Models
from users.models import Experience, Education


class ExperienceModelForm(forms.ModelForm):
    """Experice Model Form"""

    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), input_formats=settings.DATE_INPUT_FORMATS
    )

    class Meta:
        model = Experience
        fields = ("company", "title", "description", "start_date", "end_date", "current", "location")


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
