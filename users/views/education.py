""" This module contains the Education CRUD views """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

# Models
from users.models import Education

# Form
from users.forms import EducationModelForm


class EducationListView(LoginRequiredMixin, ListView):
    """Education list view"""

    template_name = "users/education/list.html"
    model = Education
    ordering = ("-created_at",)
    paginate_by = 10
    context_object_name = "educations"


class EducationCreateView(LoginRequiredMixin, CreateView):
    """Education create view"""

    template_name = "users/education/create.html"
    success_url = reverse_lazy("users:education_list")
    form_class = EducationModelForm

    def form_valid(self, form):
        """Assign the user to the education"""
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        """Return the education's owner"""
        return Education.objects.filter(user=self.request.user)


class EducationDetailView(LoginRequiredMixin, DetailView):
    """Education detail view"""

    template_name = "users/education/detail.html"
    model = Education
    context_object_name = "education"


class EducationUpdateView(LoginRequiredMixin, UpdateView):
    """Education update view"""

    template_name = "users/education/edit.html"
    form_class = EducationModelForm
    success_url = reverse_lazy("users:education_list")
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        """Assign the user to the education"""
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        """Return the education's owner"""
        return Education.objects.filter(user=self.request.user)


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    """Education delete view"""

    template_name = "users/education/delete.html"
    model = Education
    success_url = reverse_lazy("users:education_list")

    def get_queryset(self):
        """Return the education's owner"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
