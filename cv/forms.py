""" This are the form fo the CV app """

# Django
from django import forms

# Models
from users.models import Skill, Experience, Education, Project
from cv.models import CV, CVTemplate


class CVForm(forms.ModelForm):
    """CV Form"""

    Projects = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    Skills = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    Experiences = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    Educations = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(CVForm, self).__init__(*args, **kwargs)
        self.fields["Projects"].queryset = Project.objects.filter(user=self.user)
        self.fields["Skills"].queryset = Skill.objects.filter(user=self.user)
        self.fields["Experiences"].queryset = Experience.objects.filter(user=self.user)
        self.fields["Educations"].queryset = Education.objects.filter(user=self.user)

        if self.instance.pk:
            self.fields["Projects"].initial = self.instance.projects.all()
            self.fields["Skills"].initial = self.instance.skills.all()
            self.fields["Experiences"].initial = self.instance.experiences.all()
            self.fields["Educations"].initial = self.instance.educations.all()

    class Meta:
        model = CV
        fields = ["name", "profile_picture", "about_me"]


class CVTemplateForm(forms.ModelForm):
    class Meta:
        model = CVTemplate
        fields = "__all__"
        exclude = ["user", "created", "modified"]
