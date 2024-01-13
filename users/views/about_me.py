""" this file contains the views for the about"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView

# Models
from users.models import AboutMe

# Forms
# TODO : Later


class AboutMeDetailView(LoginRequiredMixin, DetailView):
    """AboutMe detail view."""

    template_name = "users/about/detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "about"
    model = AboutMe

    def get_queryset(self):
        """Restrict list of objects to the ones owned by the requesting user."""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class AboutMeUpdateView(LoginRequiredMixin, UpdateView):
    """AboutMe update view."""

    template_name = "users/about/edit.html"
    pk_url_kwarg = "pk"
    queryset = AboutMe.objects.all()
    fields = ["title", "about"]
    context_object_name = "about"
    success_url = reverse_lazy("users:about_list")


class AboutMeCreateView(LoginRequiredMixin, CreateView):
    """AboutMe create view."""

    template_name = "users/about/create.html"
    fields = ["title", "about"]
    context_object_name = "about"
    model = AboutMe
    success_url = reverse_lazy("users:about_list")

    def form_valid(self, form):
        """Save the form data."""
        about = form.save(commit=False)
        about.user = self.request.user
        about.save()
        return super().form_valid(form)


class AboutMeDeleteView(LoginRequiredMixin, DeleteView):
    """AboutMe delete view."""

    template_name = "users/about/delete.html"
    pk_url_kwarg = "pk"
    context_object_name = "about"
    model = AboutMe
    success_url = reverse_lazy("users:about_list")

    def get_queryset(self):
        """Restrict list of objects to the ones owned by the requesting user."""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class AboutMeListView(LoginRequiredMixin, ListView):
    """AboutMe list view."""

    template_name = "users/about/list.html"
    queryset = AboutMe.objects.all()
    context_object_name = "abouts"
