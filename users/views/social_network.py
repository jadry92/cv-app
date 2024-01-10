""" This file contains the social network media CRUD view """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

# Models
from users.models import SocialNetwork


class SocialNetworkListView(LoginRequiredMixin, ListView):
    """List all social networks"""

    template_name = "social_network/list.html"
    model = SocialNetwork
    context_object_name = "social_networks"


class SocialNetworkCreateView(LoginRequiredMixin, CreateView):
    """Create a social network"""

    template_name = "social_network/cretate.html"
    model = SocialNetwork
    fields = ["name", "url"]
    success_url = reverse_lazy("social:list")


class SocialNetworkDetailView(LoginRequiredMixin, DetailView):
    """Detail a social network"""

    template_name = "social_network/detail.html"
    model = SocialNetwork
    context_object_name = "social_network"


class SocialNetworkUpdateView(LoginRequiredMixin, UpdateView):
    """Update a social network"""

    template_name = "social_network/update.html"
    model = SocialNetwork
    fields = ["name", "url"]
    success_url = reverse_lazy("social:list")


class SocialNetworkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a social network"""

    template_name = "social_network/delete.html"
    model = SocialNetwork
    success_url = reverse_lazy("social:list")
