""" CV urls app """

# Django
from django.urls import path
# Views
from cv.views import CVListView

urlpatterns = [
    path("cvs/", CVListView.as_view(), name="cv_list"),
    ]
