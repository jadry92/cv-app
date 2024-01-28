""" CV Views """
# Utils
import functools
import ssl

# Django
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import FormView, ListView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import Http404

# django weasyprint
from django_weasyprint.views import WeasyTemplateResponse, WeasyTemplateResponseMixin
from django_weasyprint.utils import django_url_fetcher

# Models
from cv.models import CV, CVTemplate

# Forms
from cv.forms import CVForm


class CVListView(LoginRequiredMixin, ListView):
    """CV List View"""

    template_name = "cv/list.html"
    model = CV
    context_object_name = "cvs"

    def get_queryset(self):
        """Return the cvs for the current user."""
        return CV.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """Add the user to the context."""
        context = super().get_context_data(**kwargs)
        instance = context["cvs"]
        col_1 = []
        col_2 = []
        for i in range(len(instance)):
            if i % 2 == 0:
                col_1.append(instance[i])
            else:
                col_2.append(instance[i])

        context["col_1"] = col_1
        context["col_2"] = col_2
        return context


class CVDetailView(LoginRequiredMixin, DetailView):
    """CV Detail View"""

    template_name = "cv/detail.html"
    model = CV
    pk_url_kwarg = "pk"
    context_object_name = "cv"

    def get_context_data(self, **kwargs):
        """Add the user to the context."""
        context = super().get_context_data(**kwargs)

        return context


class CVCreateView(LoginRequiredMixin, FormView):
    """CV Create View"""

    template_name = "cv/create.html"
    form_class = CVForm
    success_url = reverse_lazy("cv:cv_list")
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user

        instance = form.save(commit=False)
        instance.save()
        instance.projects.set(form.cleaned_data["Projects"])
        instance.skills.set(form.cleaned_data["Skills"])
        instance.experiences.set(form.cleaned_data["Experiences"])
        instance.educations.set(form.cleaned_data["Educations"])
        instance.social_networks.set(form.cleaned_data["SocialNetworks"])
        temp = CVTemplate.objects.get(pk=form.cleaned_data["Template"].pk)
        temp.cv.add(instance)
        temp.save()
        instance.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(CVCreateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CVUpdateView(LoginRequiredMixin, FormView):
    """CV Update View"""

    template_name = "cv/edit.html"
    success_url = reverse_lazy("cv:cv_list")
    pk_url_kwarg = "pk"
    form_class = CVForm

    def get_object(self):
        """Return the user's cv."""
        return get_object_or_404(CV, pk=self.kwargs.get(self.pk_url_kwarg), user=self.request.user)

    def get_context_data(self, **kwargs):
        """Add the user to the context."""
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        instance = form.save(commit=False)
        instance.projects.set(form.cleaned_data["Projects"])
        instance.skills.set(form.cleaned_data["Skills"])
        instance.experiences.set(form.cleaned_data["Experiences"])
        instance.educations.set(form.cleaned_data["Educations"])
        instance.social_networks.set(form.cleaned_data["SocialNetworks"])
        instance.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        kwargs.update({"instance": self.get_object()})
        return kwargs


class CVDeleteView(LoginRequiredMixin, DeleteView):
    """CV Delete View"""

    template_name = "cv/delete.html"
    model = CV
    success_url = reverse_lazy("cv:cv_list")
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """Return the cvs for the current user."""
        return CV.objects.filter(user=self.request.user)


class CVTemplateListView(ListView):
    """CV Template List View"""

    template_name = "cv/cv_templates/list.html"
    context_object_name = "cv_templates"

    def get_queryset(self):
        """Return the cvs for the current user."""
        return CVTemplate.objects.all()


class CVTemplateDetailView(DetailView):
    """CV Template Detail View"""

    model = CVTemplate
    template_name = "cv/cv_templates/preview.html"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        """Add the user to the context."""
        context = super().get_context_data(**kwargs)
        dumy_data = {
            "user": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@text.com",
                "phone": "123456789",
                "address": "123 Main St",
                "birth_date": "1990-01-01",
            },
            "name": "cv_dumy",
            "profile_picture": "",
            "skills": {
                "all": [
                    {
                        "name": "skill name",
                        "percentage": 50,
                    }
                ]
            },
            "experiences": {
                "all": [
                    {
                        "description": "some infor about yourd education",
                        "start_date": "2021-01-01",
                        "end_date": "2021-01-01",
                        "location": "some location",
                        "title": "some title",
                        "company": "some company",
                    }
                ]
            },
            "educations": {
                "all": [
                    {
                        "description": "some infor about yourd education",
                        "start_date": "2021-01-01",
                        "end_date": "2021-01-01",
                        "location": "some location",
                        "school": "some school",
                        "degree": "some degree",
                    }
                ]
            },
            "projects": {
                "all": [
                    {
                        "description": "info about the project",
                        "title": "project title",
                        "url": "project link",
                    }
                ]
            },
            "social_networks": {
                "all": [
                    {
                        "name": "facebook",
                        "url": "https://www.facebook.com/",
                    }
                ]
            },
            "about_me": "Experienced software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success. Well-versed in technology and writing code to create systems that are reliable and user-friendly.",
        }
        context["cv"] = dumy_data
        context["template_name"] = self.object.template_name
        return context


class CVPreviewView(LoginRequiredMixin, DetailView):
    """CV Preview View"""

    template_name = "cv/cv_templates/preview.html"
    context_object_name = "cv"

    def get_object(self, queryset=None):
        """Return the user's cv."""
        return get_object_or_404(CV, id=self.kwargs.get("pk_cv"), user=self.request.user)

    def get_context_data(self, **kwargs):
        """Add the user to the context."""
        context = super().get_context_data(**kwargs)
        try:
            context["template_name"] = CVTemplate.objects.get(id=self.kwargs.get("pk_temp")).template_name
            return context
        except:
            raise Http404("Template does not exist or cv does not have a template")


def custom_url_fetcher(url, *args, **kwargs):
    # rewrite requests for CDN URLs to file path in STATIC_ROOT to use local file
    cloud_storage_url = "https://cdnjs.cloudflare.com/ajax/libs/"
    # if url.startswith(cloud_storage_url):
    #    url = "file://" + url.replace(cloud_storage_url, settings.STATIC_URL)
    return django_url_fetcher(url, *args, **kwargs)


class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to pass a kwarg to URL fetcher
    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(custom_url_fetcher, ssl_context=context)


class DownloadCVView(LoginRequiredMixin, WeasyTemplateResponseMixin, DetailView):
    """This view is to generate de cv in pdf and download"""

    pdf_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css"]
    response_class = CustomWeasyTemplateResponse

    def get_object(self, queryset=None):
        """Return the user's cv."""
        return get_object_or_404(CV, id=self.kwargs.get("pk_cv"), user=self.request.user)

    def get_context_data(self, **kwargs):
        """Add the user to the context."""
        context = super().get_context_data(**kwargs)
        try:
            self.template_name = CVTemplate.objects.get(id=self.kwargs.get("pk_temp")).template_name
            context["template_name"] = self.template_name
            context["cv"] = CV.objects.get(id=self.kwargs.get("pk_cv"), user=self.request.user)
            return context
        except:
            raise Http404("Template does not exist or cv does not have a template")
