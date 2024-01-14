""" This are the urls for the cover letter app. """

# Django
from django.urls import path

# Views
from cover_letter.views import (
    CoverLetterCreateView,
    CoverLetterDeleteView,
    CoverLetterDetailView,
    CoverLetterListView,
    CoverLetterUpdateView,
)


urlpatterns = [
    path("", CoverLetterListView.as_view(), name="list"),
    path("create/", CoverLetterCreateView.as_view(), name="create"),
    path("<int:pk>/", CoverLetterDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CoverLetterUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CoverLetterDeleteView.as_view(), name="delete"),
]
