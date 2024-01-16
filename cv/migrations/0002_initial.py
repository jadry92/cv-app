# Generated by Django 4.2.5 on 2024-01-16 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
        ("cv", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cv",
            name="about_me",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="cv", to="users.aboutme"
            ),
        ),
        migrations.AddField(
            model_name="cv",
            name="educations",
            field=models.ManyToManyField(related_name="cv", to="users.education"),
        ),
        migrations.AddField(
            model_name="cv",
            name="experiences",
            field=models.ManyToManyField(related_name="cv", to="users.experience"),
        ),
        migrations.AddField(
            model_name="cv",
            name="profile_picture",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="cv", to="users.profilepicture"
            ),
        ),
        migrations.AddField(
            model_name="cv",
            name="projects",
            field=models.ManyToManyField(related_name="cv", to="users.project"),
        ),
        migrations.AddField(
            model_name="cv",
            name="skills",
            field=models.ManyToManyField(related_name="cv", to="users.skill"),
        ),
        migrations.AddField(
            model_name="cv",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="cv", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
