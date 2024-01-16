"""
    User urls
"""
# TODO: Refactor this in different files
# Django
from django.urls import path

# User Views
from users.views import CreatePictureProfile, UserDetailView

# About views
from users.views import AboutMeCreateView, AboutMeDeleteView, AboutMeDetailView, AboutMeListView, AboutMeUpdateView

# Experience views
from users.views import (
    ExperienceCreateView,
    ExperienceDeleteView,
    ExperienceDetailView,
    ExperienceListView,
    ExperienceUpdateView,
)

# Education views
from users.views import (
    EducationCreateView,
    EducationDeleteView,
    EducationDetailView,
    EducationListView,
    EducationUpdateView,
)

# Skill views
from users.views import SkillCreateView, SkillDeleteView, SkillDetailView, SkillListView, SkillUpdateView

# social networks views
from users.views import (
    SocialNetworkCreateView,
    SocialNetworkDeleteView,
    SocialNetworkDetailView,
    SocialNetworkListView,
    SocialNetworkUpdateView,
)

# Project views
from users.views import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

app_name = "users"
urlpatterns = [
    # profile
    path("detail/<str:username>/", UserDetailView.as_view(), name="detail"),
    #    path("update/<str:username>/", UserUpdateView.as_view(), name="update"),
    # about
    path("about/", AboutMeListView.as_view(), name="about_list"),
    path("about/create/", AboutMeCreateView.as_view(), name="about_create"),
    path("about/<int:pk>/", AboutMeDetailView.as_view(), name="about_detail"),
    path("about/<int:pk>/delete/", AboutMeDeleteView.as_view(), name="about_delete"),
    path("about/<int:pk>/edit/", AboutMeUpdateView.as_view(), name="about_edit"),
    # socials
    path("social/", SocialNetworkListView.as_view(), name="social_network_list"),
    path("social/create/", SocialNetworkCreateView.as_view(), name="social_network_create"),
    path("social/<int:pk>/", SocialNetworkDetailView.as_view(), name="social_network_detail"),
    path("social/<int:pk>/delete/", SocialNetworkDeleteView.as_view(), name="social_network_delete"),
    path("social/<int:pk>/edit/", SocialNetworkUpdateView.as_view(), name="social_network_edit"),
    # projects
    path("project/", ProjectListView.as_view(), name="project_list"),
    path("project/create/", ProjectCreateView.as_view(), name="project_create"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
    path("project/<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_edit"),
    # experiences
    path("experience/", ExperienceListView.as_view(), name="experience_list"),
    path("experience/create/", ExperienceCreateView.as_view(), name="experience_create"),
    path("experience/<int:pk>/", ExperienceDetailView.as_view(), name="experience_detail"),
    path("experience/<int:pk>/delete/", ExperienceDeleteView.as_view(), name="experience_delete"),
    path("experience/<int:pk>/edit/", ExperienceUpdateView.as_view(), name="experience_edit"),
    # educations
    path("education/", EducationListView.as_view(), name="education_list"),
    path("education/create/", EducationCreateView.as_view(), name="education_create"),
    path("education/<int:pk>/", EducationDetailView.as_view(), name="education_detail"),
    path("education/<int:pk>/delete/", EducationDeleteView.as_view(), name="education_delete"),
    path("education/<int:pk>/edit/", EducationUpdateView.as_view(), name="education_edit"),
    # skills
    path("skill/", SkillListView.as_view(), name="skill_list"),
    path("skill/create/", SkillCreateView.as_view(), name="skill_create"),
    path("skill/<int:pk>/", SkillDetailView.as_view(), name="skill_detail"),
    path("skill/<int:pk>/delete/", SkillDeleteView.as_view(), name="skill_delete"),
    path("skill/<int:pk>/edit/", SkillUpdateView.as_view(), name="skill_edit"),
    # Photo TODO : Create a view for this
    path("me/<str:username>/picture/create/", CreatePictureProfile.as_view(), name="picture"),
    path("me/<str:username>/picture/update/", CreatePictureProfile.as_view(), name="picture"),
    path("me/<str:username>/", UserDetailView.as_view(), name="user_detail"),
]
