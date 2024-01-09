""" CV urls app """

# Django
from django.urls import path
# Views
from cv.views import CVListView

urlpatterns = [
    path("cvs/", CVListView.as_view(), name="cv_list"),
    path("cv_create/", CVListView.as_view(), name="cv_create"),
    path("cv/<int:pk>/", CVListView.as_view(), name="cv_detail"),
    path("cv/<int:pk>/edit/", CVListView.as_view(), name="cv_edit"),
    path("cv/<int:pk>/delete/", CVListView.as_view(), name="cv_delete"),
    path("cv/<int:pk>/download/", CVListView.as_view(), name="cv_download"),
]
