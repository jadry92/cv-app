
# Django
from django.urls import path

# Views
from ai.views import foo, AskView

app_name = "sk"

urlpatterns = [
    path("", foo ,name="foo"),
    path("ask/", AskView.as_view(), name="ask"),
]
