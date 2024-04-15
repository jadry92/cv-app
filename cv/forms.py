""" This are the form fo the CV app """

# Django
from django import forms

# Models
from users.models import Skill, Experience, Education, Project, SocialNetwork
from cv.models import CV, CVTemplate


class CVForm(forms.ModelForm):
    """CV Form"""

    projects = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    skills = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    experiences = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    educations = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    social_networks = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    template = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(CVForm, self).__init__(*args, **kwargs)
        self.fields["projects"].queryset = Project.objects.filter(user=self.user)
        self.fields["skills"].queryset = Skill.objects.filter(user=self.user)
        self.fields["experiences"].queryset = Experience.objects.filter(user=self.user)
        self.fields["educations"].queryset = Education.objects.filter(user=self.user)
        self.fields["social_networks"].queryset = SocialNetwork.objects.filter(user=self.user)
        self.fields["template"].queryset = CVTemplate.objects.all()


    def clean_template(self):
        """Check if the template is already in use."""
        template = self.cleaned_data["template"]
        return template

    class Meta:
        model = CV
        fields = ["name", "about_me", "profile_picture", "projects", "skills", "experiences", "educations", "social_networks", "template"]
        exclude = ["user"]
