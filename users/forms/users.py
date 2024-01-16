""" This file contains the form to update user's profile. """

# Django
from django import forms


class ProfileForm(forms.Form):
    """Profile/user form."""

    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    address = forms.CharField(max_length=50)
    birth_date = forms.DateField()
    phone = forms.CharField(max_length=20)
    picture_profile = forms.ImageField(required=False)

    def clean(self):
        """Clean data."""
        data = super().clean()

        return data

    def save(self):
        """Save data."""
        data = self.cleaned_data
        return data
