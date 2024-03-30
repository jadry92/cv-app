""" This view is used to display the home page of the website. """

# Django
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from job.models import Job


class HomeView(LoginRequiredMixin, TemplateView):
    """Home view."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """add jobs to context"""
        context = super().get_context_data(**kwargs)
        context["jobs"] = Job.objects.filter(status=0)

        return context
