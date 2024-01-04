"""
    Users app views
"""
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView

from django.urls import reverse
# Models
User = get_user_model()



class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """User update view."""

    template_name = "users/update.html"
    model = User
    fields = ["first_name", "last_name", "email"]
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.username
        return reverse("users:detail", kwargs={"username": username})
