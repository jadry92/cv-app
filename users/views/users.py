"""
    Users app views
"""
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView

from django.urls import reverse_lazy

# Models
from users.models import ProfilePicture

User = get_user_model()
# Forms
from users.forms import ProfileForm


class UserDetailView(LoginRequiredMixin, TemplateView):
    """User detail view."""

    template_name = "users/detail.html"
    context_object_name = "user"
    model = User

    def get_context_data(self, **kwargs):
        """Add user's profile to context."""
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["picture_profile"] = ProfilePicture.objects.filter(user=user).first()
        return context

    def get_object(self):
        """Return user's profile."""
        return self.request.user


class UserUpdateView(LoginRequiredMixin, FormView):
    """User update view."""

    template_name = "users/update.html"
    form_class = ProfileForm
    success_url = reverse_lazy("users:detail")

    def get_initial(self):
        """Return user's profile."""
        initial = super().get_initial()
        user = self.request.user

        initial["first_name"] = user.first_name
        initial["last_name"] = user.last_name
        initial["email"] = user.email
        initial["address"] = user.address
        initial["birth_date"] = user.birth_date
        initial["phone"] = user.phone
        self.pic = ProfilePicture.objects.filter(user=user).first()
        if self.pic:
            initial["picture_profile"] = self.pic.picture

        return initial

    def form_valid(self, form):
        """Save form data."""
        data = form.cleaned_data
        user = self.request.user
        picture_profile = data.pop("picture_profile")
        # creating image profile
        if picture_profile:
            pic = ProfilePicture.objects.get_or_create(user=user)
            pic[0].picture = picture_profile
            pic[0].save()

        # updating user data
        User.objects.filter(id=user.id).update(**data)

        return super().form_valid(form)
