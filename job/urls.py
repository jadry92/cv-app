""" This are the urls of the job application. """

# Django
from django.urls import path

# Views
from job.views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("<int:pk>/", JobDetailView.as_view(), name="detail"),
    path("create/", JobCreateView.as_view(), name="create"),
    path("<int:pk>/update/", JobUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", JobDeleteView.as_view(), name="delete"),
]
