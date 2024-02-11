""" This are the views for the cover letter app. """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import response
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from django.conf import settings

# Models
from cover_letter.models import CoverLetter

# OpenAI
from openai import OpenAI


class CoverLetterListView(LoginRequiredMixin, ListView):
    """This class defines the list view for the cover letter model."""

    model = CoverLetter
    template_name = "cover_letter/list.html"
    context_object_name = "cover_letters"
    ordering = ("-created_at",)


class CoverLetterCreateView(LoginRequiredMixin, CreateView):
    """This class defines the create view for the cover letter model."""

    model = CoverLetter
    fields = ["name", "text"]
    template_name = "cover_letter/create.html"
    success_url = reverse_lazy("cover_letter:cover_letter_list")

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
    fields = ["name", "text"]
    template_name = "cover_letter/edit.html"
    success_url = reverse_lazy("cover_letter:cover_letter_list")


class CoverLetterDeleteView(LoginRequiredMixin, DeleteView):
    """This class defines the delete view for the cover letter model."""

    model = CoverLetter
    template_name = "cover_letter/delete.html"
    success_url = reverse_lazy("cover_letter:cover_letter_list")


class CoverLetterSuggestionView(LoginRequiredMixin, TemplateView):
    """This class defines the suggestion view for the cover letter model."""

    model = CoverLetter
    template_name = "cover_letter/suggestion.html"

    def get_context_data(self, **kwargs):
        """Get the context data."""
        context = super().get_context_data(**kwargs)
        cover_letter = CoverLetter.objects.get(pk=self.kwargs["pk"], user=self.request.user)
        context["cover_letter"] = cover_letter
        client = OpenAI(api_key=settings.CHAT_GPT_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a highly qualified candidate for the position."},
                {
                    "role": "user",
                    "content": f"can you help me impruve my cover letter? I have written the following: {cover_letter.text}",
                },
            ],
            max_tokens=20,
        )
        context["suggestion"] = response["choices"][0]["message"]["content"]
        return context
