# Django
from django.apps import AppConfig
from django.conf import settings


class CvConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cv"

    def ready(self):
        """Load the templates into the database."""
        # Models
        from cv.models import CVTemplate

        # Utils
        import os
        import re

        try:
            temp_path = os.path.join(settings.TEMPLATES[0]["DIRS"][0], "cv/cv_templates")
            list_templates = os.listdir(temp_path)
            cv_templates_on_db = CVTemplate.objects.all()
            cv_templates_on_db_names = [cv_template.name for cv_template in cv_templates_on_db]
            for template_name in list_templates:
                if re.match(r"^template_.*.html$", template_name):
                    if template_name not in cv_templates_on_db_names:
                        template_name_path = f"cv/cv_templates/{template_name}"
                        CVTemplate.objects.create(name=template_name, template_name=template_name_path)

            return super().ready()
        except Exception as e:
            print(e)
            return super().ready()
