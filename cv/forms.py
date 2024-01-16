""" This are the form fo the CV app """

# Django
from django import forms

# Models
from cv.models import CV, CVTemplate


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = "__all__"
        exclude = ["user", "created", "modified"]


class CVTemplateForm(forms.ModelForm):
    class Meta:
        model = CVTemplate
        fields = "__all__"
        exclude = ["user", "created", "modified"]
