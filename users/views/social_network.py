""" This file contains the social network media CRUD view """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

# Models
from users.models import SocialNetwork


class SocialNetworkListView(LoginRequiredMixin, ListView):
    """List all social networks"""

    template_name = "users/social_network/list.html"
    model = SocialNetwork
    context_object_name = "social_networks"


class SocialNetworkCreateView(LoginRequiredMixin, CreateView):
    """Create a social network"""

    template_name = "users/social_network/create.html"
    model = SocialNetwork
    fields = ["name", "url"]
    success_url = reverse_lazy("users:social_network_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SocialNetworkDetailView(LoginRequiredMixin, DetailView):
    """Detail a social network"""

    template_name = "users/social_network/detail.html"
    model = SocialNetwork
    context_object_name = "social_network"


class SocialNetworkUpdateView(LoginRequiredMixin, UpdateView):
    """Update a social network"""

    template_name = "users/social_network/update.html"
    model = SocialNetwork
    fields = ["name", "url"]
    success_url = reverse_lazy("users:social_network_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SocialNetworkDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a social network"""

    template_name = "users/social_network/delete.html"
    model = SocialNetwork
    success_url = reverse_lazy("users:social_network_list")
