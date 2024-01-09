""" this file contains the views for the about"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView

# Models
from users.models import AboutMe

# Forms
# TODO : Later

class AboutMeDetailView(LoginRequiredMixin, DetailView):
    """AboutMe detail view."""
    template_name = "users/about/detail.html"
    pk_url_kwarg = "pk"
    queryset = AboutMe.objects.all()
    context_object_name = "about"


class AboutMeUpdateView(LoginRequiredMixin, UpdateView):
    """AboutMe update view."""
    template_name = "users/about/update.html"
    pk_url_kwarg = "pk"
    queryset = AboutMe.objects.all()
    fields = "__all__"
    context_object_name = "about"


class AboutMeCreateView(LoginRequiredMixin, CreateView):
    """AboutMe create view."""
    template_name = "users/about/create.html"
    fields = "__all__"
    context_object_name = "about"
    model = AboutMe


class AboutMeDeleteView(LoginRequiredMixin, DeleteView):
    """AboutMe delete view."""
    template_name = "users/about/delete.html"
    pk_url_kwarg = "pk"
    queryset = AboutMe.objects.all()
    context_object_name = "about"

class AboutMeListView(LoginRequiredMixin, ListView):
    """AboutMe list view."""
    template_name = "users/about/list.html"
    queryset = AboutMe.objects.all()
    context_object_name = "abouts"
