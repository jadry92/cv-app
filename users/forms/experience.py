""" Experience Form """

# Django
from django import forms
from django.conf import settings

# Models
from users.models import Experience


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

    def clean(self):
        """Clean data"""
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("Start date must be before end date")

        return self.cleaned_data
