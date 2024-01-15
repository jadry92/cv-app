""" CV urls app """

# Django
from django.urls import path

# Views
from cv.views import CVListView, CVDetailView, CVDeleteView, CVUpdateView, CVCreateView


app_name = "cv"

urlpatterns = [
    path("cv/", CVListView.as_view(), name="cv_list"),
    path("cv/create/", CVCreateView.as_view(), name="cv_create"),
    path("cv/<int:pk>/", CVDetailView.as_view(), name="cv_detail"),
    path("cv/<int:pk>/edit/", CVUpdateView.as_view(), name="cv_edit"),
    path("cv/<int:pk>/delete/", CVDeleteView.as_view(), name="cv_delete"),
    path("cv/<int:pk>/download/", CVListView.as_view(), name="cv_download"),
]
