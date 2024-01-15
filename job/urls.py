""" This are the urls of the job application. """

# Django
from django.urls import path

# Views
from job.views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView

app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("create/", JobCreateView.as_view(), name="job_create"),
    path("<int:pk>/update/", JobUpdateView.as_view(), name="job_update"),
    path("<int:pk>/delete/", JobDeleteView.as_view(), name="job_delete"),
]
