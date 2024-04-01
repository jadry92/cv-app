
# Django
from django import forms


class AskForm(forms.Form):
    text = forms.CharField(label="Ask something", max_length=100)
