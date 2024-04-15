""" CV Views """

# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import Http404

# django weasyprint
from django_weasyprint.views import WeasyTemplateResponse, WeasyTemplateResponseMixin, WeasyTemplateView

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


class CVCreateView(LoginRequiredMixin, CreateView):
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
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CVUpdateView(LoginRequiredMixin, UpdateView):
    """CV Update View"""

    template_name = "cv/edit.html"
    success_url = reverse_lazy("cv:cv_list")
    pk_url_kwarg = "pk"
    form_class = CVForm

    def get_queryset(self):
        """Return the user's cv."""
        return CV.objects.filter(user=self.request.user,id=self.kwargs.get(self.pk_url_kwarg))

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        initial = {}
        cv = self.get_object()
        initial["name"] = cv.name
        initial["about_me"] = cv.about_me
        initial["profile_picture"] = cv.profile_picture
        initial["projects"] = cv.projects.all()
        initial["skills"] = cv.skills.all()
        initial["experiences"] = cv.experiences.all()
        initial["educations"] = cv.educations.all()
        initial["social_networks"] = cv.social_networks.all()
        initial["template"] = [temp.id for temp in cv.template.all()]
        return initial

    def form_valid(self,form):
        """ Save the update CV """
        instance = form.save()
        templates = form.cleaned_data["template"]
        instance.template.clear()
        for temp in templates:
            temp.cv.add(instance)
            temp.save()

        return super().form_valid(form)




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


class DownloadCVView(LoginRequiredMixin, WeasyTemplateView):
    """This view is to generate de cv in pdf and download"""

    pdf_stylesheets = ["static/css/bootstrap.min.css"]


    def get_pdf_stylesheets(self):
        pdf_stylesheets = super().get_pdf_stylesheets()
        base_path = "static/css/"
        base_name = self.template_name.split("/")[-1].split(".")[0]
        pdf_stylesheets.append(base_path + base_name + ".css")
        return pdf_stylesheets


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
