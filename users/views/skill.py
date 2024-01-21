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

    def get_queryset(self):
        """Return the skill's owner"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class SkillCreateView(LoginRequiredMixin, CreateView):
    """Skill create view"""

    template_name = "users/skill/create.html"
    model = Skill
    fields = ["name", "percentage"]
    success_url = reverse_lazy("users:skill_list")

    def form_valid(self, form):
        """Assign the current user to the skill"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class SkillDetailView(LoginRequiredMixin, DetailView):
    """Skill detail view"""

    template_name = "users/skill/detail.html"
    model = Skill
    context_object_name = "skill"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """Return the skill's owner"""
        queryset = super(SkillDetailView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    """Skill update view"""

    template_name = "users/skill/edit.html"
    model = Skill
    fields = ["name", "percentage"]
    success_url = reverse_lazy("users:skill_list")
    pk_url_kwarg = "pk"

    def form_valid(self, form):
        """Assign the current user to the skill"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    """Skill delete view"""

    template_name = "users/skill/delete.html"
    model = Skill
    success_url = reverse_lazy("users:skill_list")
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """Return the skill's owner"""
        queryset = super(SkillDeleteView, self).get_queryset()
        return queryset.filter(user=self.request.user)
