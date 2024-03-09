# Celery
from config.celery import app

# Models
from job.models import JobDetails, Job

# Utils
import json
import logging
from job.utils import request_analysis


logger = logging.getLogger(__name__)


@app.task()
def create_job_details(job_id, user_id):
    """This function creates a new job details object"""

    # Get Job object

    try:
        job = Job.objects.get(pk=job_id)
        if job.raw_description == "":
            logger.warning("Raw description is empty")
        analysis, usage = request_analysis(job.raw_description)

        usage_str = ""
        if usage:
            usage_str = f"{usage.prompt_tokens} input tokens, {usage.completion_tokens} anwser tokens| Total={usage.total_tokens}"

        JobDetails.objects.create(job=job, json_detail=json.dumps(analysis), usage=usage_str)

        logger.info("analisys of the job was created")

    except Job.DoesNotExist:
        raise ValueError(f"Job with id {job_id} does not exist")
