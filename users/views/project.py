""" This file contains the Project CRUD views """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

# Models
from users.models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    """Project list view"""

    template_name = "users/project/list.html"
    model = Project
    ordering = ("-created_at",)
    paginate_by = 10
    context_object_name = "projects"

    def get_queryset(self):
        """Return the user's projects"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Project create view"""

    template_name = "users/project/create.html"
    model = Project
    fields = [
        "title",
        "description",
        "url",
    ]
    success_url = reverse_lazy("users:project_list")

    def form_valid(self, form):
        """Assign the user to the project"""
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        """Return the user's projects"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    """Project detail view"""

    template_name = "users/project/detail.html"
    model = Project
    context_object_name = "project"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """Return the user's projects"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Project update view"""

    template_name = "users/project/edit.html"
    model = Project
    fields = [
        "title",
        "description",
        "url",
    ]
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("users:project_list")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Project delete view"""

    template_name = "users/project/delete.html"
    model = Project
    success_url = reverse_lazy("users:project_list")
    pk_url_kwarg = "pk"
