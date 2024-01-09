"""
    User urls
"""

# Django
from django.urls import path

# User Views
from users.views import UserDetailView, UserUpdateView

# Abour views
from users.views import AboutMeCreateView, AboutMeDeleteView, AboutMeDetailView, AboutMeListView, AboutMeUpdateView

app_name = "users"
urlpatterns = [
    # profile
    path("detail/<str:username>/", UserDetailView.as_view(), name="detail"),
    path("update/<str:username>/", UserUpdateView.as_view(), name="update"),
    # abouts
    path("abouts/", AboutMeListView.as_view(), name="abouts_list"),
    path("about-create/", AboutMeCreateView.as_view(), name="about_create"),
    path("about/<pk:int>/", AboutMeDetailView.as_view(), name="about_detail"),
    path("about/<pk:int>/delete/", AboutMeDeleteView.as_view(), name="about_delete"),
    path("about/<pk:int>/edit/", AboutMeUpdateView.as_view(), name="about_edit"),
    # socials
    path("socials/", UserDetailView.as_view(), name="socials_list"),
    path("social-create/", UserDetailView.as_view(), name="social_create"),
    path("social/<pk:int>/", UserDetailView.as_view(), name="social_detail"),
    path("social/<pk:int>/delete/", UserDetailView.as_view(), name="social_delete"),
    path("social/<pk:int>/edit/", UserDetailView.as_view(), name="social_edit"),
    # projects
    path("projects/", UserDetailView.as_view(), name="projects_list"),
    path("project-create/", UserDetailView.as_view(), name="project_create"),
    path("project/<pk:int>/", UserDetailView.as_view(), name="project_detail"),
    path("project/<pk:int>/delete/", UserDetailView.as_view(), name="project_delete"),
    path("project/<pk:int>/edit/", UserDetailView.as_view(), name="project_edit"),
    # experiences
    path("experiences/", UserDetailView.as_view(), name="experiences_list"),
    path("experience-create/", UserDetailView.as_view(), name="experience_create"),
    path("experience/<pk:int>/", UserDetailView.as_view(), name="experience_detail"),
    path("experience/<pk:int>/delete/", UserDetailView.as_view(), name="experience_delete"),
    path("experience/<pk:int>/edit/", UserDetailView.as_view(), name="experience_edit"),
    # educations
    path("educations/", UserDetailView.as_view(), name="educations_list"),
    path("education-create/", UserDetailView.as_view(), name="education_create"),
    path("education/<pk:int>/", UserDetailView.as_view(), name="education_detail"),
    path("education/<pk:int>/delete/", UserDetailView.as_view(), name="education_delete"),
    path("education/<pk:int>/edit/", UserDetailView.as_view(), name="education_edit"),
    # skills
    path("skills/", UserDetailView.as_view(), name="skills_list"),
    path("skill-create/", UserDetailView.as_view(), name="skill_create"),
    path("skill/<pk:int>/", UserDetailView.as_view(), name="skill_detail"),
    path("skill/<pk:int>/delete/", UserDetailView.as_view(), name="skill_delete"),
    path("skill/<pk:int>/edit/", UserDetailView.as_view(), name="skill_edit"),
    # Photo
    path("picture/", UserDetailView.as_view(), name="picture"),
    path("picture/update/", UserDetailView.as_view(), name="picture_update"),
]
