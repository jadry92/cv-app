""" This are the views of the job application. """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.shortcuts import redirect

# Models
from job.models import Job, JobDetails
from cv.models import CV

# Forms
from job.forms import JobModelForm, JobAppliedForm

# Utils
from job.tasks import create_job_details
import json


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
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """This is the query set of the job application."""
        return Job.objects.filter(pk=self.kwargs[self.pk_url_kwarg], user=self.request.user)

    def get_context_data(self, **kwargs):
        """This is the context data of the job application."""

        context = super().get_context_data(**kwargs)
        list_detail = JobDetails.objects.filter(job__id=self.kwargs[self.pk_url_kwarg])
        if list_detail:
            for i in range(len(list_detail)):
                list_detail[i].json_detail = json.loads(list_detail[i].json_detail)

        context["job_details"] = list_detail
        context["cvs"] = CV.objects.filter(user=self.request.user)
        return context


class JobCreateView(LoginRequiredMixin, CreateView):
    """This is the create view of the job application."""

    template_name = "job/create.html"
    success_url = reverse_lazy("job:job_list")
    form_class = JobModelForm

    def get_queryset(self):
        """This is the query set of the job application."""
        return Job.objects.filter(user=self.request.user)

    def form_valid(self, form):
        """This is the form validation of the job application."""

        form.instance.user = self.request.user

        # Save the form
        job = form.save()
        create_job_details.delay(job.id, self.request.user.pk)
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UpdateView):
    """This is the update view of the job application."""

    template_name = "job/edit.html"
    success_url = reverse_lazy("job:job_list")
    form_class = JobModelForm
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """This is the query set of the job application."""
        return Job.objects.filter(pk=self.kwargs[self.pk_url_kwarg], user=self.request.user)

    def form_valid(self, form):
        """This is the form validation of the job application."""

        form.instance.user = self.request.user
        job = form.save()

        create_job_details.delay(job.id, self.request.user.pk)
        return super(JobUpdateView, self).form_valid(form)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    """This is the delete view of the job application."""

    model = Job
    template_name = "job/delete.html"
    success_url = reverse_lazy("job:list")


class JobAnalysisDetail(LoginRequiredMixin, TemplateView):

    template_name = "job/analysis.html"

    def get_context_data(self, **kwargs):
        """This is the context data of the job application."""
        context = super().get_context_data(**kwargs)
        pk = self.request.GET.get("job", None)
        print(pk)
        if pk == None:
            redirect("job:job_list")
        job = Job.objects.get(pk=pk, user=self.request.user)
        context["job"] = job
        list_detail = JobDetails.objects.filter(job=job)
        if list_detail:
            for i in range(len(list_detail)):
                list_detail[i].json_detail = json.loads(list_detail[i].json_detail)

        context["job_details"] = list_detail
        return context


class JobAppliedView(LoginRequiredMixin, FormView):
    """This is the applyed view of the job application."""

    template_name = "job/applied.html"
    success_url = reverse_lazy("job:job_list")
    form_class = JobAppliedForm
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """This is the query set of the job application."""
        return Job.objects.filter(pk=self.kwargs[self.pk_url_kwarg], user=self.request.user)

    def get_context_data(self, **kwargs):
        """This is the context data of the job application."""
        context = super().get_context_data(**kwargs)
        context["job"] = Job.objects.get(pk=self.kwargs[self.pk_url_kwarg], user=self.request.user)
        return context

    def form_valid(self, form):
        """This is the form validation of the job application."""
        cleaned_data = form.cleaned_data
        job = Job.objects.get(pk=self.kwargs[self.pk_url_kwarg], user=self.request.user)
        job.status = cleaned_data["status"]
        job.cv = cleaned_data["cv_used"]
        job.cover_letter = cleaned_data["cover_letter_used"]
        job.save()

        return super().form_valid(form)
