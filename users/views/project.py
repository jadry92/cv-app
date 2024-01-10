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
    ordering = ("-created",)
    paginate_by = 10
    context_object_name = "projects"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Project create view"""

    template_name = "users/project/create.html"
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("users:projects_list")


class ProjectDetailView(LoginRequiredMixin, DetailView):
    """Project detail view"""

    template_name = "users/project/detail.html"
    model = Project
    context_object_name = "project"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Project update view"""

    template_name = "users/project/update.html"
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("users:projects_list")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Project delete view"""

    template_name = "users/project/delete.html"
    model = Project
    success_url = reverse_lazy("users:projects_list")
