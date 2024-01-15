""" This are the views of the job application. """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Models
from job.models import Job


class JobListView(LoginRequiredMixin, ListView):
    """This is the list view of the job application."""

    model = Job
    template_name = "job/list.html"
    context_object_name = "jobs"
    ordering = ("-created_at",)


class JobDetailView(LoginRequiredMixin, DetailView):
    """This is the detail view of the job application."""

    model = Job
    template_name = "job/detail.html"
    context_object_name = "job"


class JobCreateView(LoginRequiredMixin, CreateView):
    """This is the create view of the job application."""

    model = Job
    template_name = "job/create.html"
    fields = ["name", "notes", "url", "applied", "status", "company"]
    success_url = reverse_lazy("job:list")

    def form_valid(self, form):
        """This is the form validation of the job application."""

        form.instance.user = self.request.user
        return super(JobCreateView, self).form_valid(form)


class JobUpdateView(LoginRequiredMixin, UpdateView):
    """This is the update view of the job application."""

    model = Job
    template_name = "job/update.html"
    fields = ["name", "notes", "url", "applied", "status", "company"]
    success_url = reverse_lazy("job:list")

    def form_valid(self, form):
        """This is the form validation of the job application."""

        form.instance.user = self.request.user
        return super(JobUpdateView, self).form_valid(form)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    """This is the delete view of the job application."""

    model = Job
    template_name = "job/delete.html"
    success_url = reverse_lazy("job:list")
