""" admin view for cv app """

# Django
from django.contrib import admin

# Models
from cv.models import CV

admin.site.register(CV)
