""" This file contain the taks that are going to be executed by the celery worker """

# Django
from django.core.exceptions import ObjectDoesNotExist

# Models
from job.models import JobDetails
from cv.models import CV
from cover_letter.models import CoverLetterGPT3, CoverLetter

# Utils
import logging
from cover_letter.utils import request_suggestion_for_cover_letter


def cover_letter_suggestion(job_analysis_id, cv_id, cover_letter_id):
    """This function sends a request to the GPT-3 API to get a suggestion for a cover letter"""
    logger = logging.getLogger(__name__)
    try:
        cv = CV.objects.get(id=cv_id)
        job_details = JobDetails.objects.get(id=job_analysis_id)
        suggestion, usage = request_suggestion_for_cover_letter(job_details.get_json_detail(), cv.get_cv_str())
        cover_letter = CoverLetter.objects.get(id=cover_letter_id)
        cover_letter_gpt = CoverLetterGPT3.objects.create(
            cover_letter=cover_letter, name=f"Cover letter for {job_details.job.name}", text=suggestion, usage=usage
        )

        return cover_letter_gpt.pk

    except ObjectDoesNotExist as e:
        logger.error(f"The job or cv does not exist: {e}")
