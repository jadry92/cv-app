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

app_name = "cover_letter"

urlpatterns = [
    path("", CoverLetterListView.as_view(), name="cover_letter_list"),
    path("create/", CoverLetterCreateView.as_view(), name="cover_letter_create"),
    path("<int:pk>/", CoverLetterDetailView.as_view(), name="cover_letter_detail"),
    path("<int:pk>/update/", CoverLetterUpdateView.as_view(), name="cover_letter_edit"),
    path("<int:pk>/delete/", CoverLetterDeleteView.as_view(), name="cover_letter_delete"),
]
