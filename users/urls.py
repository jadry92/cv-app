"""
    User urls
"""

# Django
from django.urls import path

# Views
from users.views import UserDetailView, UserUpdateView

app_name = "users"
urlpatterns = [
    path("detail/<str:username>/", UserDetailView.as_view(), name="detail"),
    path("update/<str:username>/", UserUpdateView.as_view(), name="update"),
]
