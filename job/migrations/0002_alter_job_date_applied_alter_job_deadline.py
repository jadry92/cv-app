# Generated by Django 4.2.5 on 2024-01-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="date_applied",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
    ]
