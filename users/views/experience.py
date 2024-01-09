""" This file containt the experience views"""

# Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from users.models import Experience

# Forms
# TODO: Create the experience form


class ExperienceListView(LoginRequiredMixin, ListView):
    """This class return the experience list"""
    model = Experience
    template_name = "users/experience/list.html"
    context_object_name = "experiences"


class ExperienceDetailView(LoginRequiredMixin, DetailView):
    """This class return the experience detail"""
    model = Experience
    template_name = "users/experience/detail.html"
    context_object_name = "experience"
    pk_url_kwarg = "pk"

class ExperienceCreateView(LoginRequiredMixin, CreateView):
    """This class return the experience create"""
    model = Experience
    template_name = "users/experience/create.html"
    fields = "__all__"
    success_url = "/experience/list"

class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    """This class return the experience update"""
    model = Experience
    template_name = "users/experience/update.html"
    fields = "__all__"
    pk_url_kwarg = "pk"
    success_url = "/experience/list"

class ExperienceDeleteView(LoginRequiredMixin, DeleteView):
    """This class return the experience delete"""
    model = Experience
    template_name = "users/experience/delete.html"
    pk_url_kwarg = "pk"
    success_url = "/experience/list"

