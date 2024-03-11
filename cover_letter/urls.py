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
    CoverLetterSuggestionView,
)

app_name = "cover_letter"

urlpatterns = [
    path("", CoverLetterListView.as_view(), name="cover_letter_list"),
    path("create/", CoverLetterCreateView.as_view(), name="cover_letter_create"),
    path("create-automatic/", CoverLetterCreateView.as_view(), name="cover_letter_create_automatic"),
    path("<int:pk>/", CoverLetterDetailView.as_view(), name="cover_letter_detail"),
    path("<int:pk>/edit/", CoverLetterUpdateView.as_view(), name="cover_letter_edit"),
    path("<int:pk>/suggestion/", CoverLetterSuggestionView.as_view(), name="cover_letter_suggestion"),
    path("<int:pk>/delete/", CoverLetterDeleteView.as_view(), name="cover_letter_delete"),
]
