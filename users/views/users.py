"""
    Users app views
"""
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView

from django.urls import reverse_lazy

# Models
User = get_user_model()
# Forms
from users.forms import ProfileForm


class UserDetailView(LoginRequiredMixin, TemplateView):
    """User detail view."""

    template_name = "users/detail.html"
    context_object_name = "user"
    model = User

    def get_object(self):
        """Return user's profile."""
        return self.request.user


class UserUpdateView(LoginRequiredMixin, FormView):
    """User update view."""

    template_name = "users/update.html"
    form_class = ProfileForm
    success_url = reverse_lazy("users:detail")

    def get_object(self):
        """Return user's profile."""
        return self.request.user
