# Generated by Django 4.2.5 on 2024-01-21 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cover_letter", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="coverletter",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="cover_letter", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
