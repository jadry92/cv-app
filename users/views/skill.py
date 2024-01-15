""" This file contains the Skill CRUD views """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

# Models
from users.models import Skill


class SkillListView(LoginRequiredMixin, ListView):
    """Skill list view"""

    template_name = "users/skill/list.html"
    model = Skill
    ordering = ("-created_at",)
    paginate_by = 10
    context_object_name = "skills"


class SkillCreateView(LoginRequiredMixin, CreateView):
    """Skill create view"""

    template_name = "users/skill/create.html"
    model = Skill
    fields = "__all__"
    success_url = reverse_lazy("users:skills_list")


class SkillDetailView(LoginRequiredMixin, DetailView):
    """Skill detail view"""

    template_name = "users/skill/detail.html"
    model = Skill
    context_object_name = "skill"


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    """Skill update view"""

    template_name = "users/skill/update.html"
    model = Skill
    fields = "__all__"
    success_url = reverse_lazy("users:skills_list")


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    """Skill delete view"""

    template_name = "users/skill/delete.html"
    model = Skill
    success_url = reverse_lazy("users:skills_list")
