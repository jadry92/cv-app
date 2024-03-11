""" This are the views for the cover letter app. """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView, RedirectView
from django.conf import settings

# Models
from cover_letter.models import CoverLetter
from job.models import Job, JobDetails
from cv.models import CV

# Utils
from openai import OpenAI
import json
from urllib.parse import urlencode

# Tasks
from cover_letter.tasks import cover_letter_suggestion


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

    def get_context_data(self, **kwargs):
        """Get the context data."""
        context = super().get_context_data(**kwargs)

        # Adding job information to the context
        context["jobs"] = Job.objects.filter(user=self.request.user, status=0).only("pk", "name")
        return context


class CoverLetterDetailView(LoginRequiredMixin, DetailView):
    """This class defines the detail view for the cover letter model."""

    model = CoverLetter
    template_name = "cover_letter/detail.html"
    context_object_name = "cover_letter"

    def get_context_data(self, **kwargs):
        """Get the context data."""
        context = super().get_context_data(**kwargs)

        # Adding job information to the context
        context["jobs"] = Job.objects.filter(user=self.request.user, status=0).only("pk", "name")
        return context


class CoverLetterUpdateView(LoginRequiredMixin, UpdateView):
    """This class defines the update view for the cover letter model."""

    model = CoverLetter
    fields = ["name", "text"]
    template_name = "cover_letter/edit.html"
    success_url = reverse_lazy("cover_letter:cover_letter_list")

    def get_context_data(self, **kwargs):
        """Get the context data."""
        context = super().get_context_data(**kwargs)
        job_id = self.request.GET.get("job")
        if job_id:
            job = Job.objects.filter(pk=job_id, user=self.request.user).first()
            if not job:
                return context
            context["job"] = job
            list_detail = JobDetails.objects.filter(job=job)
            if list_detail:
                for i in range(len(list_detail)):
                    list_detail[i].json_detail = json.loads(list_detail[i].json_detail)

            context["job_details"] = list_detail
        else:
            context["jobs"] = Job.objects.filter(user=self.request.user, status=0).only("pk", "name")
        return context


class CoverLetterCreateAutomaticView(LoginRequiredMixin, RedirectView):
    """This class defines the create automatic view for the cover letter model."""

    permanent = True
    url = reverse_lazy("cover_letter:cover_letter_create")

    def post(self, request, *args, **kwargs):
        """Create Cover Letter base on a suggestion."""
        job_id = request.POST.get("job")
        job = get_object_or_404(Job, pk=job_id, user=request.user)
        job_details = JobDetails.objects.filter(job=job).first()
        cv_id = request.POST.get("cv")
        cv = get_object_or_404(CV, pk=cv_id, user=request.user)
        if not job_details:
            return redirect(reverse("cover_letter:cover_letter_create"))

        cover_letter = CoverLetter.objects.create(
            user=request.user,
            name=f"Cover Letter for {job.name}",
            text="",
        )
        cover_letter_gpt_id = cover_letter_suggestion(job_details.pk, cv.pk, cover_letter.pk)

        base_url = reverse("cover_letter:cover_letter_edit", kwargs={"pk": cover_letter.pk})
        query_string = urlencode({"job": job.pk, "cv": cv.pk, "gpt_id": cover_letter_gpt_id})

        url = f"{base_url}?{query_string}"
        return HttpResponsePermanentRedirect(url)


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
        )
        context["suggestion"] = response.choices[0].message.content
        return context
