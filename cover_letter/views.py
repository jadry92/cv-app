""" This are the views for the cover letter app. """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

# Models
from cover_letter.models import CoverLetter


class CoverLetterListView(LoginRequiredMixin, ListView):
    """This class defines the list view for the cover letter model."""

    model = CoverLetter
    template_name = "cover_letter/list.html"
    context_object_name = "cover_letters"
    ordering = ["-created_at"]


class CoverLetterCreateView(LoginRequiredMixin, CreateView):
    """This class defines the create view for the cover letter model."""

    model = CoverLetter
    fields = ["name", "text", "url_job"]
    template_name = "cover_letter/create.html"
    success_url = reverse_lazy("cover_letter:list")

    def form_valid(self, form):
        """Save the form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class CoverLetterDetailView(LoginRequiredMixin, DetailView):
    """This class defines the detail view for the cover letter model."""

    model = CoverLetter
    template_name = "cover_letter/detail.html"
    context_object_name = "cover_letter"


class CoverLetterUpdateView(LoginRequiredMixin, UpdateView):
    """This class defines the update view for the cover letter model."""

    model = CoverLetter
    fields = ["name", "text", "url_job"]
    template_name = "cover_letter/update.html"
    success_url = reverse_lazy("cover_letter:list")


class CoverLetterDeleteView(LoginRequiredMixin, DeleteView):
    """This class defines the delete view for the cover letter model."""

    model = CoverLetter
    template_name = "cover_letter/delete.html"
    success_url = reverse_lazy("cover_letter:list")
