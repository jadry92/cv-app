""" CV Views """

# Django
from django.views.generic import TemplateView


class CVListView(TemplateView):
    """ CV List View """
    template_name = "cv/cv_list.html"
