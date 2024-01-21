""" This module contains the Education CRUD views """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

# Models
from users.models import Education


class EducationListView(LoginRequiredMixin, ListView):
    """Education list view"""

    template_name = "users/education/list.html"
    model = Education
    ordering = ("-created_at",)
    paginate_by = 10
    context_object_name = "educations"


class EducationCreateView(LoginRequiredMixin, CreateView):
    """Education create view"""

    template_name = "users/education/create.html"
    model = Education
    fields = ["degree", "description", "location", "start_date", "end_date", "school"]
    success_url = reverse_lazy("users:education_list")

    def form_valid(self, form):
        """Assign the user to the education"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationDetailView(LoginRequiredMixin, DetailView):
    """Education detail view"""

    template_name = "users/education/detail.html"
    model = Education
    context_object_name = "education"


class EducationUpdateView(LoginRequiredMixin, UpdateView):
    """Education update view"""

    template_name = "users/education/edit.html"
    model = Education
    fields = ["degree", "description", "location", "start_date", "end_date", "school"]
    success_url = reverse_lazy("users:education_list")

    def form_valid(self, form):
        """Assign the user to the education"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    """Education delete view"""

    template_name = "users/education/delete.html"
    model = Education
    success_url = reverse_lazy("users:education_list")

    def get_queryset(self):
        """Return the education's owner"""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
