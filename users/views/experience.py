""" This file containt the experience views"""

# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from users.models import Experience

# Forms
from users.forms import ExperienceModelForm


class ExperienceListView(LoginRequiredMixin, ListView):
    """This class return the experience list"""

    model = Experience
    template_name = "users/experience/list.html"
    context_object_name = "experiences"

    def get_queryset(self):
        """Return the user's experiences"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ExperienceDetailView(LoginRequiredMixin, DetailView):
    """This class return the experience detail"""

    model = Experience
    template_name = "users/experience/detail.html"
    context_object_name = "experience"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """Return the user's experiences"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ExperienceCreateView(LoginRequiredMixin, CreateView):
    """This class return the experience create"""

    form_class = ExperienceModelForm
    template_name = "users/experience/create.html"
    success_url = reverse_lazy("users:experience_list")

    def form_valid(self, form):
        """Assign the user to the experience"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    """This class return the experience update"""

    model = Experience
    template_name = "users/experience/edit.html"
    fields = [
        "title",
        "company",
        "location",
        "description",
        "current",
        "start_date",
        "end_date",
    ]
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("users:experience_list")

    def get_queryset(self):
        """Return the user's experiences"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def form_valid(self, form):
        """Assign the user to the experience"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperienceDeleteView(LoginRequiredMixin, DeleteView):
    """This class return the experience delete"""

    model = Experience
    template_name = "users/experience/delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("users:experience_list")

    def get_queryset(self):
        """Return the user's experiences"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
