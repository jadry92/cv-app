# Generated by Django 4.2.5 on 2024-01-21 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cv", "0001_initial"),
        ("cover_letter", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("notes", models.TextField()),
                ("url", models.URLField()),
                ("company", models.URLField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "No Applied"),
                            (1, "Applied"),
                            (2, "Interview"),
                            (3, "Rejected"),
                            (4, "Offer"),
                            (5, "Accepted"),
                            (6, "No call"),
                        ],
                        default=0,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date_applied", models.DateField(null=True)),
                ("deadline", models.DateField(null=True)),
                (
                    "cover_letter",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="job",
                        to="cover_letter.coverletter",
                    ),
                ),
                (
                    "cv",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="job", to="cv.cv"
                    ),
                ),
            ],
        ),
    ]
