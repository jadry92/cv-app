""" CV Views """

# Django
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Models
from cv.models import CV

class CVListView(ListView):

    """ CV List View """
    template_name = "cv/list.html"
    model = CV


class CVDetailView(DetailView):
    """ CV Detail View """
    template_name = "cv/detail.html"
    model = CV
    pk_url_kwarg = "pk"


class CVCreateView(CreateView):
    """ CV Create View """
    template_name = "cv/create.html"
    model = CV
    fields = "__all__"
    success_url = "cv:cv_list"
    pk_url_kwarg = "pk"


class CVUpdateView(UpdateView):
    """ CV Update View """
    template_name = "cv/update.html"
    model = CV
    fields = "__all__"
    success_url = "cv:cv_list"
    pk_url_kwarg = "pk"


class CVDeleteView(DeleteView):
    """ CV Delete View """
    template_name = "cv/delete.html"
    model = CV
    success_url = "cv:cv_list"
