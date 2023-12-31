# Generated by Django 4.2.5 on 2024-01-05 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0002_user_address_user_birth_date_user_phone_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CV",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "about_me",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="cv", to="users.aboutme"
                    ),
                ),
                ("educations", models.ManyToManyField(related_name="cv", to="users.education")),
                ("experiences", models.ManyToManyField(related_name="cv", to="users.experience")),
                (
                    "profile_picture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="cv", to="users.profilepicture"
                    ),
                ),
                ("projects", models.ManyToManyField(related_name="cv", to="users.project")),
                ("skills", models.ManyToManyField(related_name="cv", to="users.skill")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="cv", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "CV",
                "verbose_name_plural": "CVs",
                "ordering": ["user", "name"],
            },
        ),
    ]
