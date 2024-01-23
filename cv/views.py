""" CV Views """

# Django
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, DetailView

# Models
from cv.models import CV, CVTemplate

# Forms
from cv.forms import CVForm, CVTemplateForm


class CVListView(ListView):

    """CV List View"""

    template_name = "cv/list.html"
    model = CV


class CVDetailView(DetailView):
    """CV Detail View"""

    template_name = "cv/detail.html"
    model = CV
    pk_url_kwarg = "pk"


class CVCreateView(CreateView):
    """CV Create View"""

    template_name = "cv/create.html"
    form_class = CVForm
    success_url = reverse_lazy("cv:cv_list")
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        self.object = form.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(CVCreateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CVUpdateView(UpdateView):
    """CV Update View"""

    template_name = "cv/update.html"
    model = CV
    fields = "__all__"
    success_url = reverse_lazy("cv:cv_list")
    pk_url_kwarg = "pk"


class CVDeleteView(DeleteView):
    """CV Delete View"""

    template_name = "cv/delete.html"
    model = CV
    success_url = reverse_lazy("cv:cv_list")


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
