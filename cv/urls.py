""" CV urls app """

# Django
from django.urls import path

# Views
from cv.views import (
    CVListView,
    CVDetailView,
    CVDeleteView,
    CVUpdateView,
    CVCreateView,
    CVTemplateListView,
    CVTemplateDetailView,
    CVPreviewView,
    DownloadCVView,
)


app_name = "cv"

urlpatterns = [
    path("cv/", CVListView.as_view(), name="cv_list"),
    path("cv/create/", CVCreateView.as_view(), name="cv_create"),
    path("cv/<int:pk_cv>/download/<int:pk_temp>/", DownloadCVView.as_view(), name="cv_download"),
    path("cv/<int:pk_cv>/preview/<int:pk_temp>/", CVPreviewView.as_view(), name="cv_preview"),
    path("cv/<int:pk>/", CVDetailView.as_view(), name="cv_detail"),
    path("cv/<int:pk>/edit/", CVUpdateView.as_view(), name="cv_edit"),
    path("cv/<int:pk>/delete/", CVDeleteView.as_view(), name="cv_delete"),
    path("cv/<int:pk>/download/", CVListView.as_view(), name="cv_download"),
    path("cv/templates/", CVTemplateListView.as_view(), name="cv_template_list"),
    path("cv/templates/<int:pk>/", CVTemplateDetailView.as_view(), name="cv_template_detail"),
]
