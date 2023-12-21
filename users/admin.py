# Django
from django.contrib import admin
from django.contrib.auth import get_user_model

# Models
User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
