""" This are the urls of the job application. """

# Django
from django.urls import path

# Views
from job.views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    JobAnalysisDetail,
    JobAppliedView,
)

app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("create/", JobCreateView.as_view(), name="job_create"),
    path("<int:pk>/edit/", JobUpdateView.as_view(), name="job_edit"),
    path("<int:pk>/delete/", JobDeleteView.as_view(), name="job_delete"),
    path("<int:pk>/applied/", JobAppliedView.as_view(), name="job_applied"),
    path("analysis/", JobAnalysisDetail.as_view(), name="job_analysis"),
]
