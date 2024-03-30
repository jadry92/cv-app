
# Django
from django.urls import path

# Views
from . import view


urlpatterns = [
    path("", view.foo , name="foo"),
]
