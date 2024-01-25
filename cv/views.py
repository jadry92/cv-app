""" CV Views """

# Django
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# Models
from cv.models import CV, CVTemplate

# Forms
from cv.forms import CVForm, CVTemplateForm


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
        form.save()

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

    template_name = "cv/template_list.html"
    model = CVTemplate


class CVTemplateDetailView(DetailView):
    """CV Template Detail View"""

    template_name = "cv/template_detail.html"
    model = CVTemplate
    pk_url_kwarg = "pk"


class CVTemplateReadView(FormView):
    """CV Template Read View"""

    template_name = "cv/template_read.html"
    form_class = CVTemplateForm
    success_url = reverse_lazy("cv:cv_templates_list")
    pk_url_kwarg = "pk"

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(CVTemplateReadView, self).get_form_kwargs()
        kwargs["template"] = CVTemplate.objects.get(pk=self.kwargs["pk"])
        return kwargs
